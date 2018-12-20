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

import numpy as np
from interactions import InteractionsEngine
from reputation import ReputationEngine


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

@command('simulate1')
def simulate1(graph_path):
    np.seterr(all='raise')
    interactions = InteractionsEngine()
     
    # create a network of behaving nodes
    # create some bad nodes trying to infiltrate
    # estimate the cost of obtaining the trust of all good nodes
    good_nodes = [str(i) for i in range(10)]
    hub_node = '100'
    bad_nodes = ['10']
    
    # create interactions between good nodes
    # initial vouches of trust
    for nid in good_nodes:
        source = nid
        value = 50
        interactions.insert([
            (nid,      hub_node, value),
            (hub_node, nid,      value)
        ])

        for target in good_nodes:
            if target != nid:
                pass
                # interactions.insert([
                #     (source, target, value) 
                # ])
                
    
    # for nid in bad_nodes:
    #     source = nid
    #     value = 1
    #     for target in good_nodes:
    #         if target != nid:
    #             interactions.insert([
    #                 (source, target, value) 
    #             ])
    
    interactions.insert([
        ('0', '10', 1),
        ('1', '10', 1),
        ('2', '10', 1),
        ('3', '10', 1),
        ('4', '10', 1),
        # ('1', '10', 200),
        # ('2', '10', 1),
    ])

    rep = ReputationEngine(interactions)
    rep.converge()
    for nid in good_nodes:
        print(rep.rep(nid, '10'))
        print(rep.rep('10', nid))
    # print(rep.rep('0', '10') - rep.rep('10', '0'))
    # print()

# load_all_graphs()

# print(sys.argv)
if __name__ == '__main__':
    # Run()
#     render('networks/1-simple.interactions')
    simulate1('networks/1-simple.interactions')