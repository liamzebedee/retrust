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

    for (i, j) in np.ndindex(E.shape[0], E.shape[1]):
        total_ev[i,j] = E[i,j].sum()

        b,d,u = R[i,j]

        total_ev[i,j] *= np.sqrt(b)
        
        if i == j:
            total_ev[i,j] = 0.

    normalised_ev = np.full(
        (E.shape[0], E.shape[1]),
        0.,
        dtype=np.float32
    )

    for (i, j) in np.ndindex(E.shape[0], E.shape[1]):
        normalised_ev[i,j] = total_ev[i,j] / total_ev[i,:].sum()

    print(normalised_ev)
    print(total_ev)
    # raise

    # print(total_ev)
    eigenvalues, eigenvectors = LA.eig(normalised_ev)
    print(eigenvalues)
    print(eigenvectors)
    print("principal", eigenvectors[0])
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
    quorums = optimize.fixed_point(
        f_E, 
        total_ev, 
        args=(np.copy(total_ev),), 
        # method="iteration",
        # xtol=1e-5
    )

    print(quorums)



def f_E(x, A):
    E = x.copy()

    # # fill diagonal
    # for i in np.ndindex(E.shape[0]):
    #     E[i,i] = 1
    

    for (i, j) in np.ndindex(x.shape[0], x.shape[1]):
        # g = np.copy(A[i,j])
        g = E[i,j].copy()

        for k in range(x.shape[0]):
            g += E[i,k] * A[k,j]

        
        E[i,j] = g / E[i,:].sum()
        
        #     g = opinion_add(
        #         g, 
        #         opinion_mult(R[i,k], A[k,j])
        #     )

        # E[i,j] = ((1 - d) / np.size(A[i,:])) * (x[i,j] + A[i,:].mean()) + d
        # E[i,j] = (x[i,] + A[i,:].mean())
        # E[i,j] = A[i,j] + E[:,].mean()
    
    

    # fig, ax = plt.subplots()
    # ax.matshow(x[:,:,0], cmap=plt.cm.Blues)
    
    
    
    # for (i, j) in np.ndindex(x.shape[0], x.shape[1]):
    #     t = np.array2string(x[i, j, 0], precision=3, separator=',', suppress_small=True).split('.')[1]
    #     text = ax.text(j, i, t,
    #                 ha="center", va="center", color="w")

    return E


# if __name__ == '__main__':
