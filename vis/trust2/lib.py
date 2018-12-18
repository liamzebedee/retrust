import numpy as np
from scipy import optimize




# Evidence and opinions
# ---------------------

def _opinion(b, d, u):
    return np.array((b, d, u), dtype='float')

# Dogmatic opinions
B = _opinion(1, 0, 0)
D = _opinion(0, 1, 0)
U = _opinion(0, 0, 1)

def opinion(b, d, u):
    assert(b + d + u == 1)
    # exclude dogmatics
    assert(0 <= b < 1)
    assert(0 <= d < 1)
    assert(0 <= u < 1)
    return _opinion(b, d, u)


def to_opinion(evidence_val):
    # Incorporate minimum evidence threshold
    x = _opinion(0, 0, C)

    # Set the pos/neg evidence
    if evidence_val >= 0:
        x[0] = evidence_val
    else:
        x[1] = -1 * evidence_val
    
    # Normalise
    x /= x.sum()
    
    return x

def positive_ev(x):
    (b, _, u) = x
    return C * (b / u)

def negative_ev(x):
    (_, d, u) = x
    return C * (d / u)

def total_ev(x):
    return positive_ev(x) + negative_ev(x)

def opinion_scalar_mult(a, x):
    (b, d, u) = x
    divisor = a * (b + d) + u
    x[0] *= a
    x[1] *= a
    x /= divisor
    return x

def opinion_mult(x, y):
    return generic_discount(x, y)

def opinion_add(x, y):
    return consensus(x, y)

# Consensus
# ---------

def consensus(x, y):
    (x_b, x_d, x_u) = x
    (y_b, y_d, y_u) = y

    divisor = (x_u + y_u) - (x_u * y_u)
    b = ( x_u * y_b  +  y_u * x_b ) / divisor
    d = ( x_u * y_d  +  y_u * x_d ) / divisor
    u = x_u * y_u / divisor
    return _opinion(b, d, u)


# Discounting
# -----------

def generic_discount(x, y):
    return opinion_scalar_mult(evidence_transfer_scalar(x), y)

# theta = max(positive_ev(any X))
theta = 0
def configure_ebsl(reputations):
    # theta = reputations[:, :, 0]
    # pos = 
    pass

def specific_discount(x, y):
    return opinion_scalar_mult((positive_ev(x) * theta), y)

# g(x) in paper
def evidence_transfer_scalar(x):
    b = x[0]
    return np.sqrt(b)
    # return b


# Reputation convergence
# ----------------------


# R: reputation matrix
def f_R(x, A):
    R = x

    # square
    assert(R.shape[0] == R.shape[1])

    # R_ij = A_ij + iter(k: R_ik * A_kj)
    # return matrix_plus(f_R, matrix_mult())
    # users = R.shape[0]

    for (i, j) in np.ndindex(R.shape[0], R.shape[1]):
        # sum_ = np.array(
        #     opinion_mult(R[i,k], A[k,j]) for k in np.ndindex(R.shape[1])
        # )
        g = A[i,j]
        
        for k in range(j):
            g = opinion_add(
                g, 
                opinion_mult(R[i,k], A[k,j])
            )

        R[i,j] = g

        # R[i,j] = opinion_add(
        #     A[i,j], 
        #     np.apply_along_axis(opinion_add, 0, sum_)
        # )
    
    return R



# Soft threshold on amount of evidence to accept at minimum
# / uncertainty constant
C = 2



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
    
    def get_evidence(self):
        return self.conn.execute('''
            SELECT DISTINCT source, target, SUM(value) as evidence
            FROM interactions
            GROUP BY source, target
        ''').fetchall()

def converge_worldview(interactions_data):
    # 
    # 1. Convert interactions to evidence (aggregation)
    # 
    interactions = InteractionsEngine()
    interactions.insert(interactions_data)
    users = interactions.get_users()

    evidence = interactions.get_evidence()



    # 
    # 2. Convert evidence to opinions and build reputations matrix.
    # 
    shape = (
        len(users),
        len(users),
        3
    )
    reputations = np.zeros(shape, dtype=float)

    # fill diagonal
    for i in np.ndindex(shape[0]):
        reputations[i,i] = U

    # remap user id's to indices for use in matrix
    user_idxs = list(map(lambda x: x[0], users))
    # user_idxs
    
    for (src, target, val) in evidence:
        i = user_idxs.index(src)
        j = user_idxs.index(target)

        reputations[i, j] = to_opinion(val)

    # 
    # 3. Converge opinions matrix.
    # 
    configure_ebsl(reputations)
    direct_opinions = np.copy(reputations)
    worldview = optimize.fixed_point(
        f_R, 
        reputations, 
        args=(direct_opinions,), 
        xtol=1e-4
    )

    # evidence = 

    return worldview