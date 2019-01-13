from os.path import abspath
import json
import sys
import itertools


from shared import numpy_helpers
from shared import matplotlib_helpers

from retrust.quorum import calc_quorum
from retrust.interactions import InteractionsEngine
from visualisation.reputation import VisualisedEBSLReputationEngine

from simulation.helpers import NodeIdGenerator


def main():
    interactions = InteractionsEngine()
    node_ids = NodeIdGenerator()

    good_nodes = node_ids(2)
    hub_node = node_ids(1)
    
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

    rep = VisualisedEBSLReputationEngine(interactions)


if __name__ == '__main__':
    main()
