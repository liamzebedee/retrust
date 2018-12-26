import numpy as np
from scipy import optimize
from functools import reduce



# Evidence and opinions
# ---------------------

# Soft threshold on amount of evidence to accept at minimum
# / uncertainty constant
C = 2.0

def _opinion(b, d, u):
    # assert(b + d + u == 1)
    return np.array((b, d, u), dtype='float64')

# Dogmatic opinions
B = _opinion(1., 0, 0)
D = _opinion(0, 1., 0)
U = _opinion(0, 0, 1.)

def opinion(b, d, u):
    # exclude dogmatics
    assert(0 <= b < 1)
    assert(0 <= d < 1)
    assert(0 <= u < 1 or (b,d,u) == (0,0,1))
    return _opinion(b, d, u)

def to_opinion(positive, negative, total):
    # Incorporate minimum evidence threshold
    
    # x = _opinion(0, 0, 1.)
    x = np.array(
        (positive, negative, C), 
        dtype='float64'
    )

    # x[0] = float(positive)
    # x[1] = float(negative)
    # x[2] = C

    # Normalise
    x /= x.sum()
    
    return opinion(*x)

def to_evidence(x):
    pos = C * (x[0] / x[2])
    neg = C * (x[1] / x[2])
    ev = np.array((pos, neg))
    return ev
	# return [[[constant*(M[i][j][0]/M[i][j][2]), constant*(M[i][j][1]/M[i][j][2])] for j in range(len(M[i]))] for i in range(len(M))]
    

def positive_ev(x):
    (b, _, u) = x
    return C * (b / u)

def negative_ev(x):
    (_, d, u) = x
    return C * (d / u)

def total_ev(x):
    return positive_ev(x) + negative_ev(x)


# Discounting
# -----------

def opinion_scalar_mult(a, x):
    # Scalar mult basically multiplies against (b,d)
    # And then normalises.
    (b, d, u) = x
    divisor = a * (b + d) + u
    return opinion(b*a / divisor, d*a / divisor, u / divisor)

def opinion_mult(x, y):
    return generic_discount(x, y)

def generic_discount(x, y):
    return opinion_scalar_mult(
        evidence_transfer_scalar(x), 
        y
    )

# theta = max(positive_ev(any X))
theta = 0
def configure_ebsl(reputations):
    # theta = reputations[:, :, 0]
    pass

def specific_discount(x, y):
    return opinion_scalar_mult((positive_ev(x) * theta), y)

# g(x) in paper
def evidence_transfer_scalar(x):
    b = x[0]
    return np.sqrt(b)
    # return b


# Consensus
# ---------

def opinion_add(x, y):
    (x_b, x_d, x_u) = x
    (y_b, y_d, y_u) = y

    divisor = (x_u + y_u) - (x_u * y_u)
    b = ( x_u * y_b  +  y_u * x_b ) / divisor
    d = ( x_u * y_d  +  y_u * x_d ) / divisor
    u = x_u * y_u / divisor
    return opinion(b, d, u)
    



# Reputation convergence
# ----------------------


import numpy as np
import matplotlib.pyplot as plt

# R: reputation matrix
f_R_i = 0
def f_R(x, A):
    global f_R_i
    f_R_i += 1
    R = np.copy(x)

    # square
    assert(R.shape[0] == R.shape[1])

    for (i, j) in np.ndindex(R.shape[0], R.shape[1]):
        # op = R[i,j]

        # R[i,j] = A[i,j] + reduce(
        #     opinion_add,
        #     [opinion_mult(R[i,k], A[k,j]) for k in range(R.shape[0])],
        #     # np.copy(R[i,j])
        # )
        # g = np.copy(A[i,j])

        # g = reduce(
        #     opinion_add,
        #     [opinion_mult(R[i,k], A[k,j]) for k in range(j)],
        #     np.copy(R[i,j])
        # )
        # g = A[i,j]
        
        
        g = np.copy(A[i,j])
        
        for k in range(R.shape[0]):
            g = opinion_add(
                g, 
                opinion_mult(R[i,k], A[k,j])
            )

        # R[i,j] = opinion_add(g, opinion(0.1, 0, 0.9))
        # R[i,j] = opinion_scalar_mult(.7, g)
        R[i,j] = g

    
    # fill diagonal
    for i in np.ndindex(R.shape[0]):
        R[i,i] = U
    
    fig, ax = plt.subplots()
    ax.matshow(x[:,:,0], cmap=plt.cm.Blues)
    
    # # We want to show all ticks...
    # ax.set_xticks(np.arange(len(farmers)))
    # ax.set_yticks(np.arange(len(vegetables)))
    # # ... and label them with the respective list entries
    # ax.set_xticklabels(farmers)
    # ax.set_yticklabels(vegetables)

    # # Rotate the tick labels and set their alignment.
    # plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
    #         rotation_mode="anchor")
    
    
    for (i, j) in np.ndindex(R.shape[0], R.shape[1]):
        t = np.array2string(x[i, j, 0], precision=3, separator=',', suppress_small=True).split('.')[1]
        text = ax.text(j, i, t,
                    ha="center", va="center", color="w")
    plt.savefig(f'networks/{f_R_i}.repmatrix.png')

    return R


def converge_worldview(interactions):
    # 
    # 1. Convert interactions to evidence (aggregation)
    # 
    users = interactions.get_users()
    evidence = interactions.get_evidence()
    # print(evidence)
    f_R_i = 0

    # 
    # 2. Convert evidence to opinions and build reputations matrix.
    # 
    shape = (
        len(users),
        len(users),
        3
    )
    reputations = np.full(
        shape, 
        U,
        dtype=np.float64
    )

    # # fill diagonal
    # for i in np.ndindex(shape[0]):
    #     reputations[i,i] = U

    # remap user id's to indices for use in matrix
    user_idxs = list(map(lambda x: x[0], users))


    for (src, target, positive, negative, total) in evidence:
        i = user_idxs.index(src)
        j = user_idxs.index(target)

        reputations[i, j] = to_opinion(positive, negative, total)

    # 
    # 3. Converge opinions matrix.
    # 
    configure_ebsl(reputations)
    direct_opinions = np.copy(reputations)
    worldview = optimize.fixed_point(
        f_R, 
        reputations, 
        args=(direct_opinions,), 
        method="iteration",
        # xtol=1e-5
    )
    print("worldview", worldview)

    evidence = np.full(
        (
            len(users),
            len(users),
            2
        ),
        np.array((0, 0)),
        dtype=np.int32
    )

    for (i, j) in np.ndindex(worldview.shape[0], worldview.shape[1]):
        evidence[i,j] = to_evidence(worldview[i,j])

    fig, ax = plt.subplots()
    ax.matshow(evidence[:,:,0], cmap=plt.cm.Blues)
    plt.savefig(f'networks/evidence.pos.png')

    fig, ax = plt.subplots()
    ax.matshow(evidence[:,:,1], cmap=plt.cm.Blues)
    plt.savefig(f'networks/evidence.neg.png')

    # for (src, target, positive, negative, total) in evidence:
    #     i = user_idxs.index(src)
    #     j = user_idxs.index(target)

    #     reputations[i, j] = to_opinion(positive, negative, total)


    return worldview, evidence