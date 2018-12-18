import json
from os.path import abspath

def load():
    interactions = None
    opinions = None
    evidence = None

    with open(abspath('./interactions.json'), 'r') as f:
        interactions = json.load(f)
    with open(abspath('./opinions.json'), 'r') as f:
        opinions = json.load(f)
    with open(abspath('./evidence.json'), 'r') as f:
        evidence = json.load(f)

# from pathlib import Path
from graphs import graph

import sys
from commandr import command, Run

@command('render')
def render(graph_path):
    graph(graph_path)
    # paths = list(Path('..').glob('networks/*.dot'))
    # for p in paths:
        # graph(p)

# load_all_graphs()

# print(sys.argv)
if __name__ == '__main__':
    # Run()
    graph('networks/1-simple.interactions')