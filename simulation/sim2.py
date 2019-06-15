from os.path import abspath
import json
import sys
import itertools


from shared import numpy_helpers
from shared import matplotlib_helpers

from retrust.quorum import calc_quorum
from retrust.interactions import InteractionsEngine
from ebsl.reputation import EBSLReputationEngine

from simulation.helpers import NodeIdGenerator

import numpy as np


def simulate_rounds():
    # what we do here
    # is simulate whether re-using the previous state of the matrix
    # can work
    

def simulate1():
    interactions = InteractionsEngine()

    node_ids = NodeIdGenerator()

    good_nodes = node_ids(10)
    other_friends = node_ids(10)
    hub_node = node_ids(1)

    for nid in other_friends:
        value = 2
        for target in good_nodes:
            interactions.insert([
                (nid,      target, value),
                (target, nid,      value)
            ])
        
    interactions.insert([
        (other_friends[0], good_nodes[0], 2),
        (other_friends[0], good_nodes[1], 2),
        (good_nodes[1], other_friends[0], 2),
    ])
    
    # create interactions between good nodes
    # initial vouches of trust
    for nid in good_nodes:
        source = nid
        value = 2
        hub_value = len(good_nodes)
        interactions.insert([
            (nid,      hub_node, value),
            (hub_node, nid,      value)
        ])

        for target in good_nodes:
            if target != nid:
                # pass
                interactions.insert([
                    (source, target, hub_value),
                    (target, source, hub_value) 
                ])
    
    interactions.insert([
        # (good_nodes[1], good_nodes[0], 20000),
        # (good_nodes[2], good_nodes[1], 20000)
    ])

    rep = EBSLReputationEngine(interactions)
    
    # print(rep.R)
    # np.savetxt("R.txt", rep.R)

    # calc_quorum(rep.R, rep.E)

if __name__ == '__main__':
    # Run()
    # print(sys.argv)
    simulate1()