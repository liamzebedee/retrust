from simulation.helpers import NodeIdGenerator
gen_node_ids = NodeIdGenerator()

class User:
    def __init__(self):
        self.id = gen_node_ids(1)

class Rider(User):
    def __init__(self):
        super().__init__()

class Driver(User):
    def __init__(self):
        super().__init__()


