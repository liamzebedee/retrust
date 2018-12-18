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
B = _opinion(1, 0, 0)
D = _opinion(0, 1, 0)
U = _opinion(0, 0, 1)

def opinion(b, d, u):
    # exclude dogmatics
    assert(0 <= b < 1)
    assert(0 <= d < 1)
    assert(0 <= u < 1)
    return _opinion(b, d, u)

# + 75
# - 75
#   2
# total = 152
# 75 / 152 = 0.49
# 75 / 152 = 0.49
# 2 / 152  = 0.013
# 
# alternatively
# 0 / 


def to_opinion(positive, negative, total):
    # Incorporate minimum evidence threshold
    x = _opinion(0, 0, 1)

    # # Set the pos/neg evidence
    # if evidence_val >= 0:
    #     x[0] = evidence_val
    # else:
    #     x[1] = -1 * evidence_val
    x[0] = float(positive)
    x[1] = float(negative)
    x[2] = C

    # Normalise
    x /= x.sum()
    
    return x

def positive_ev(x):
    (b, _, u) = x
    return C * (b / u)

def negative_ev(x):
    (_, d, u) = x
    return C * (d / u)

def total_ev(x):
    return positive_ev(x) + negative_ev(x)

# div = scalar*(ox[0]+ox[1])+ox[2]
# return [x/div for x in [scalar*ox[0], scalar*ox[1], ox[2]]]

def opinion_scalar_mult(a, x):
    (b, d, u) = x
    # np.copy(x)
    
    # new_x = opinion(b, d, u)
    
    divisor = a * (b + d) + u
    # new_x[0] *= a
    # new_x[1] *= a
    # new_x /= divisor
    return _opinion(b*a / divisor, d*a / divisor, u / divisor)

def opinion_mult(x, y):
    return generic_discount(x, y)

def opinion_add(x, y):
    return consensus(x, y)

# Consensus
# ---------

def consensus(x, y):
    (x_b, x_d, x_u) = x
    (y_b, y_d, y_u) = y

    divisor = (x_u + y_u) - (x_u * y_u)
    b = ( x_u * y_b  +  y_u * x_b ) / divisor
    d = ( x_u * y_d  +  y_u * x_d ) / divisor
    u = x_u * y_u / divisor
    return _opinion(b, d, u)



# Discounting
# -----------


def generic_discount(x, y):
    return opinion_scalar_mult(
        evidence_transfer_scalar(x), 
        y
    )

# theta = max(positive_ev(any X))
theta = 0
def configure_ebsl(reputations):
    # theta = reputations[:, :, 0]
    # pos = 
    pass

def specific_discount(x, y):
    return opinion_scalar_mult((positive_ev(x) * theta), y)

# g(x) in paper
def evidence_transfer_scalar(x):
    b = x[0]
    return np.sqrt(b)
    # return b


# Reputation convergence
# ----------------------


# R: reputation matrix
# def f_R(x):
def f_R(x, A):
    # # fill diagonal
    # for i in np.ndindex(x.shape[0]):
    #     x[i,i] = U
    
    R = np.copy(x)
    # R = x

    # square
    assert(R.shape[0] == R.shape[1])

    # R_ij = A_ij + sum(iter(k: R_ik * A_kj))
    # return matrix_plus(f_R, matrix_mult())
    # users = R.shape[0]

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

        R[i,j] = g
    


    
    # fill diagonal
    for i in np.ndindex(R.shape[0]):
        R[i,i] = U
    
    return R


# R, A
# def matrixtimes(R, A, plus=operator.add, times=operator.mul):
# 	return [
# 		[
# 			reduce(plus, list(
# 				map(times, 
# 					R[i], [A[k][j] for k in range(len(A[0]))])
# 				)
# 			) for j in range(len(A))
#         ] for i in range(len(R))
# 	]

# def matrixplus(A, B, plus=operator.add):
# 	return [list(map(plus, A[i],B[i])) for i in range(len(A))]



# from interactions import InteractionsEngine

def converge_worldview(interactions):
    # 
    # 1. Convert interactions to evidence (aggregation)
    # 
    # interactions = InteractionsEngine()
    # interactions.insert(interactions_data)
    users = interactions.get_users()
    evidence = interactions.get_evidence()
    print(evidence)


    # 
    # 2. Convert evidence to opinions and build reputations matrix.
    # 
    shape = (
        len(users),
        len(users),
        3
    )
    reputations = np.zeros(shape, dtype=np.float64)

    # fill diagonal
    for i in np.ndindex(shape[0]):
        reputations[i,i] = U

    # remap user id's to indices for use in matrix
    user_idxs = list(map(lambda x: x[0], users))
    # user_idxs
    
    for (src, target, positive, negative, total) in evidence:
        i = user_idxs.index(src)
        j = user_idxs.index(target)

        reputations[i, j] = to_opinion(positive, negative, total)

    # 
    # 3. Converge opinions matrix.
    # 
    configure_ebsl(reputations)
    direct_opinions = np.copy(reputations)
    # print("initial:")
    # print(direct_opinions)
    worldview = optimize.fixed_point(
        f_R, 
        reputations, 
        args=(direct_opinions,), 
        # method="iteration",
        xtol=1e-2
    )
    print("worldview", worldview)

    evidence = []

    return worldview, evidence