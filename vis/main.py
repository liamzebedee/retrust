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

np.set_printoptions(precision=4)
np.set_printoptions(suppress=True)


@command('render')
def render(graph_path):
    g1 = graph(graph_path, converge_worldview_og)
    print("\n")
    g2 = graph(graph_path, converge_worldview)

    diff = g2.opinions - g1.opinions

    print("G1")
    print(g1.opinions)
    print("G2")
    print(g2.opinions)

    # paths = list(Path('..').glob('networks/*.dot'))
    # for p in paths:
        # graph(p)

# load_all_graphs()

# print(sys.argv)
if __name__ == '__main__':
    # Run()
    render('networks/1-simple.interactions')
    # graph('networks/1-simple.interactions')