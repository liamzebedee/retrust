import numpy as np
from scipy import optimize
from functools import reduce

import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from pygraphviz import *

from numpy import linalg as LA


# Given a set of nodes N
# and interactions between them
# Determine each node's relative "influence" in the group
# As a weighted average of all node interactions

np.set_printoptions(precision=4)
np.set_printoptions(suppress=True)

import networkx as nx



def calc_quorum(R, E):
    # print(E.shape)
    np.savetxt("old/E.csv", E[:,:,0], delimiter=",", fmt="%1.4f")
    np.savetxt("old/R.csv", R[:,:,0], delimiter=",")

    total_ev = np.full(
        (E.shape[0], E.shape[1]),
        0.,
        dtype=np.int32
    )

    print(E)

    personalization = {}

    for (i, j) in np.ndindex(E.shape[0], E.shape[1]):
        b,d,u = R[i,j]
        total_ev[i,j] = max(E[i,j].sum(), 0) * np.sqrt(b)

        # personalization[j] = (R[5,j])[0]
        
        # if i == j:
        #     total_ev[i,j] = 0.

    # print(personalization)

    normalised_ev = np.full(
        (E.shape[0], E.shape[1]),
        0.,
        dtype=np.float32
    )

    # for (i, j) in np.ndindex(E.shape[0], E.shape[1]):
    #     # normalised_ev[i,j] = total_ev[i,j] / total_ev[:,j].mean()

    #     # normalised_ev[i,j] = (total_ev[i,j] - total_ev[:,j].mean()) / np.sqrt(total_ev[:,j].var())
    #     print(i,j, total_ev[:,i].mean(), np.sqrt(total_ev[:,i].var()) )

    #     normalised_ev[i,j] =  ( total_ev[i,j] - total_ev[:,i].mean() )  / np.sqrt(total_ev[:,i].var())

    # normalise evidence using batch norm
    # for (i,) in np.ndindex(E.shape[0]):
    #     # print( total_ev[:,i])
    #     # print( total_ev[i,:])

    #     # print(total_ev[:,i].mean())
    #     # print(np.sqrt(total_ev[:,i].var()))

    #     # print(total_ev[i,:].mean())
    #     # print(np.sqrt(total_ev[i,:].var()))

    #     # normalised_ev[i] -= total_ev[:,i].mean()
    #     # normalised_ev[i] /= np.sqrt(total_ev[:,i].var())

    #     normalised_ev[i] -= total_ev[i,:].mean()
    #     normalised_ev[i] /= np.sqrt(total_ev[i,:].var())

    
    # total_ev /= total_ev.sum(axis=1)
    # print(normalised_ev[:,0].sum())
    # print(normalised_ev[:,3].sum())

    print(total_ev)
    # print(normalised_ev)
    # raise

    # print(total_ev)
    # eigenvalues, eigenvectors = LA.eig(normalised_ev)
    # print(eigenvalues)
    # print(eigenvectors)
    # print("principal", eigenvectors[0])

    # ind = eigenvalues.argsort()
    # eigenvector of largest eigenvalue at ind[-1], normalized
    # largest = np.array(eigenvectors[:, ind[-1]]).flatten().real
    # norm = float(largest.sum())
    # pageranks = dict(zip(G, map(float, largest / norm)))
    # print(largest, norm)
    # print(pageranks)


    # np.savetxt("eigenvalues.csv", w, delimiter=",")
    # np.savetxt("eigenvectors.csv", v, delimiter=",")

    # return (w,v)

    G = nx.Graph()
    for (i, j) in np.ndindex(E.shape[0], E.shape[1]):
        G.add_weighted_edges_from([
            (i, j, total_ev[i,j])
            # (i, j, normalised_ev[i,j])
        ])

    ranks_pr = nx.algorithms.link_analysis.pagerank_numpy(
        G, 
        alpha=1,
    )

    ranks = np.ndarray(shape=(E.shape[0]), dtype=np.float32)
    for i, (k, v) in enumerate(ranks_pr.items()):
        ranks[int(k)] = float(v)

    print(ranks)

    def f_E(x, A):
        # E = x.copy()

        # for i in range(E.shape[0]):
        #     # for (i, j) in np.ndindex(E.shape[0], E.shape[1]):
        #     # g = np.copy(E[i,j])
        #     g = 0.

        #     for k in range(E.shape[0]):
        #         # g += E[i,k] / A[k,:].sum()
        #         E[i,k] = x[i,k] / x[k,:].sum()
            
                # g += E[i,k] * A[k,j]
                # g += E[i,k] * A[k,j]

                # g = opinion_add(
                #     g, 
                #     opinion_mult(R[i,k], A[k,j])
                # )

            # E[i,j] = g

        # fig, ax = plt.subplots()
        # ax.matshow(x[:,:,0], cmap=plt.cm.Blues)
        
        
        
        # for (i, j) in np.ndindex(x.shape[0], x.shape[1]):
        #     t = np.array2string(x[i, j, 0], precision=3, separator=',', suppress_small=True).split('.')[1]
        #     text = ax.text(j, i, t,
        #                 ha="center", va="center", color="w")

        return x

    # quorums = optimize.fixed_point(
    #     f_E, 
    #     total_ev, 
    #     args=(np.copy(total_ev),), 
    #     # method="iteration",
    #     # xtol=1e-5
    # )

    # print(quorums)






# if __name__ == '__main__':
