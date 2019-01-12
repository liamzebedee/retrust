# import pickle

# interactions = {}

# with open("sets/loc-brightkite_edges.txt", "r") as f:
#     from_, to = f.read().split('\t')

import networkx as nx
# network = nx.Graph()
from numpy import genfromtxt
import numpy as np
import sys

import pickle

data = genfromtxt('datasets/sets/soc-sign-bitcoinotc.csv', delimiter=',')

from collections import defaultdict
# Members of Bitcoin OTC rate other members in a scale of -10 (total distrust) to +10 (total trust) in steps of 1

# remove timestamp last col
data = data[:, :-1]

# convert to graph
# interactions = defaultdict(lambda: 0)
# interactions = []

# SOURCE: node id of source, i.e., rater
# TARGET: node id of target, i.e., ratee
# RATING: the source's rating for the target, ranging from -10 to +10 in steps of 1

def normalize(rating):
    min_ = -10
    max_ = 10
    return rating

# print(np.amax(data, axis=0))
# print(np.amax(data, axis=1))

# sys.exit(0)

n = 6006
# n = 20
interactions = np.zeros([n, n], dtype=np.uint8)


for (source, target, rating) in data.tolist():
    source = int(source)
    target = int(target)
    rating = int(normalize(rating))
    interactions[source, target] = rating

# post process with default values
np.save('networks/soc-sign-bitcoinotc.interactions.npy', interactions)


interactions2 = []
for (idx, val) in np.ndenumerate(interactions):
    interactions2.append([
        idx[0],
        idx[1],
        val
    ])

pickle.dumps('networks/soc-sign-bitcoinotc.interactions.pickle', interactions2)

# with open('networks/soc-sign-bitcoinotc.interactions.npy', 'w') as f:
#     np.save(f, interactions)
    # for (source, target) in np.ndindex(*interactions.shape):
    #     rating = interactions[source, target]
    #     f.write(f'{source} {target} {rating}\n')

# import network of ratings
# build categories of sybil networks
# prove that the general sybil attack is intractable with x economic resources

