
import numpy as np
from interactions import InteractionsEngine
from trust2.lib import converge_worldview

class ReputationEngine():
    def __init__(self, interactions):
        self.interactions = interactions
    
    def converge(self):
        self.R, self.E = converge_worldview(self.interactions)

    def user(self, user_id):
        users = self.interactions.get_users_list()
        return users.index(user_id)
    
    def perspective(self, user_id):
        return self.R[self.user(user_id)]
    
    def rep(self, perspective, user_id):
        return self.R[self.user(perspective), self.user(user_id)]