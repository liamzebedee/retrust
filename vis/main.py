import json
from os.path import abspath

# def load():
#     interactions = None
#     opinions = None
#     evidence = None

#     with open(abspath('./interactions.json'), 'r') as f:
#         interactions = json.load(f)
#     with open(abspath('./opinions.json'), 'r') as f:
#         opinions = json.load(f)
#     with open(abspath('./evidence.json'), 'r') as f:
#         evidence = json.load(f)

# from pathlib import Path
from graphs import graph

import sys
from commandr import command, Run


from trust.calc import converge_worldview as converge_worldview_og
from trust2.lib import converge_worldview
from trust2.quorum import calc_quorum

import numpy as np
from interactions import InteractionsEngine
from reputation import ReputationEngine

import itertools
np.set_printoptions(precision=4)
np.set_printoptions(suppress=True)


@command('render')
def compare_algos(graph_path):
    g1 = graph(graph_path, converge_worldview_og)
    print("\n")
    g2 = graph(graph_path, converge_worldview)

    diff = g2.opinions - g1.opinions

    print("G1")
    print(g1.opinions)
    print("G2")
    print(g2.opinions)

def id_generator():
    id = 0
    while(True):
        yield str(id)
        id += 1

@command('simulate1')
def simulate1(graph_path):
    np.seterr(all='raise')
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

    rep = ReputationEngine(interactions)
    rep.converge()
    # for nid in good_nodes:
    #     print(rep.rep(nid, '10'))
    #     print(rep.rep('10', nid))

    # print(rep.rep('0', '10') - rep.rep('10', '0'))
    # print()


    E = calc_quorum(rep.R, rep.E)
    print(E)

# load_all_graphs()

# print(sys.argv)
if __name__ == '__main__':
    # Run()
    # render('networks/1-simple.interactions')
    simulate1('networks/1-simple.interactions')