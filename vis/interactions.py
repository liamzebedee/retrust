import sqlite3

class InteractionsEngine:
    def __init__(self):
        conn = sqlite3.connect(':memory:')
        
        c = conn.cursor()
        c.execute('''
            CREATE TABLE interactions
            (source text, target text, value integer)
        ''')

        conn.commit()

        self.conn = conn
        self.c = c
    
    def insert(self, interactions):
        for (source, target, value) in interactions:
            self.conn.execute('''INSERT INTO interactions VALUES (?, ?, ?)''', (source, target, value))
        self.conn.commit()

    def get_users(self):
        users = self.conn.execute('''
        select distinct id from (
            SELECT DISTINCT source AS id
            FROM interactions

            UNION

            SELECT DISTINCT target AS id
            FROM interactions
        )
        ORDER BY id
        ''')
        return users.fetchall()
    
    def get_users_list(self):
        return list(map(lambda x: x[0], self.get_users()))

    def get_evidence(self):
        return self.conn.execute('''
            SELECT 
                DISTINCT source, target, 
                SUM(case when value>=0 then value else 0 end) as positive,
                SUM(case when value<0  then abs(value) else 0 end) as negative,
                SUM(ABS(value)) as total
            FROM interactions
            GROUP BY source, target
        ''').fetchall()
    
    def get_interactions_list(self):
        rows = self.conn.execute('''
            SELECT *
            FROM interactions
        ''')
        return [[source, target, value] for (source, target, value) in rows]
