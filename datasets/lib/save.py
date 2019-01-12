import numpy as np
import pickle

x = np.load('networks/soc-sign-bitcoinotc.interactions.npy')
# x = x[:100, :100]

interactions2 = []
i = 0
for (idx, val) in np.ndenumerate(x):
    i += 1
    print(i)
    interactions2.append([
        idx[0],
        idx[1],
        val
    ])

print('x')

with open('networks/soc-sign-bitcoinotc.interactions.pickle', 'bw') as f:
    pickle.dump(
        interactions2, 
        f,
        -1
    )