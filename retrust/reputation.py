class ReputationEngine():
    def __init__(self, interactions):
        pass
    
    # Get the reputation opinions of every user in the system from a's perspective
    def perspective(self, a):
        raise NotImplementedError
    
    # Gets b's reputation from a's perspective
    def reputation_of(self, a, b):
        raise NotImplementedError