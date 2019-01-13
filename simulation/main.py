from os.path import abspath
import json
import sys
import itertools


from shared import numpy_helpers
from shared import matplotlib_helpers

from retrust.quorum import calc_quorum
from retrust.interactions import InteractionsEngine
from ebsl.reputation import EBSLReputationEngine

from helpers import id_generator

def simulate1(graph_path):
    interactions = InteractionsEngine()

    node_ids = id_generator()

    # create a network of behaving nodes
    # create some bad nodes trying to infiltrate
    # estimate the cost of obtaining the trust of all good nodes
    good_nodes = list(itertools.islice(node_ids, 10))
    hub_node = next(node_ids)
    bad_nodes = list(itertools.islice(node_ids, 10))
    
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
                
    
    # for nid in bad_nodes:
    #     source = nid
    #     value = 1
    #     for target in good_nodes:
    #         if target != nid:
    #             interactions.insert([
    #                 (source, target, value) 
    #             ])
    

    # generate a sybil network of high trust
    sybil_net = list(itertools.islice(node_ids, 10))
    for nid in sybil_net:
        value = 2
        hub_value = len(good_nodes)

        for target in sybil_net:
            interactions.insert([
                (nid, target, 20),
            ])

    interactions.insert([
        # ('1', '0', 1),
        # ('2', '0', 1),
        # ('3', '0', 1),
        # ('4', '0', 1),


        # ('4', '3', -10),
        # ('3', '8', 1),
        # ('3', '10', 1),
        # ('4', '10', 1),
        # ('1', '10', 200),
        # ('2', '10', 1),
    ])

    rep = EBSLReputationEngine(interactions)
    # for nid in good_nodes:
    #     print(rep.rep(nid, '10'))
    #     print(rep.rep('10', nid))

    # print(rep.rep('0', '10') - rep.rep('10', '0'))
    # print()
    calc_quorum(rep.R, rep.E)

if __name__ == '__main__':
    # Run()
    # print(sys.argv)
    simulate1('networks/1-simple.interactions')