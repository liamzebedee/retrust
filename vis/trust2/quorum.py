import numpy as np
from scipy import optimize
from functools import reduce

import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from pygraphviz import *

# Given a set of nodes N
# and interactions between them
# Determine each node's relative "influence" in the group
# As a weighted average of all node interactions

def calc_quorum(R, E):
    print(E.shape)
    np.savetxt("E.csv", E[:,:,0], delimiter=",", fmt="%1.4f")
    # np.savetxt("R.csv", R[:,:,0], delimiter=",")
    return optimize.fixed_point(
        f_E, 
        E, 
        args=(E,), 
        # method="iteration",
        # xtol=1e-5
    )


d = 0.85
def f_E(x, A):

    E = x.copy()

    # fill diagonal
    for i in np.ndindex(E.shape[0]):
        E[i,i] = 1
    

    for (i, j) in np.ndindex(x.shape[0], x.shape[1]):
        # g = np.copy(A[i,j])
        
        # for k in range(x.shape[0]):
        #     g = opinion_add(
        #         g, 
        #         opinion_mult(R[i,k], A[k,j])
        #     )

        # E[i,j] = ((1 - d) / np.size(A[i,:])) * (x[i,j] + A[i,:].mean()) + d
        # E[i,j] = (x[i,] + A[i,:].mean())
        E[i,j] = A[i,j] + x[i,:].mean()
    
    # fig, ax = plt.subplots()
    # ax.matshow(x[:,:,0], cmap=plt.cm.Blues)
    
    
    
    # for (i, j) in np.ndindex(x.shape[0], x.shape[1]):
    #     t = np.array2string(x[i, j, 0], precision=3, separator=',', suppress_small=True).split('.')[1]
    #     text = ax.text(j, i, t,
    #                 ha="center", va="center", color="w")

    return E