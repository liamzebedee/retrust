import numpy as np

from ebsl.lib import *
from retrust.reputation import ReputationEngine

class ListToMatrixIndexMapper:
    def __init__(self, l):
        self.l = l
        self.idxs = list(map(lambda x: x[0], l))
    
    def __call__(self, id):
        # remap user id's to indices for use in matrix
        return self.idxs.index(id)

class EBSLReputationEngine(ReputationEngine):
    def __init__(self, interactions):
        # self.interactions = interactions

        users = interactions.get_users()
        self.users_idx = ListToMatrixIndexMapper(users)
        
        shape = (
            len(users),
            len(users),
            3
        )

        # 
        # 1. Convert interactions to evidence (aggregation)
        # 
        extracted_evidence = interactions.get_evidence()

        # print(evidence)
        f_R_i = 0
    

        # 
        # 2. Convert evidence to opinions and build reputations matrix.
        # 
        reputations = np.full(
            shape, 
            U,
            dtype=np.float64
        )

        initial_evidence = np.full(
            (
                len(users),
                len(users),
                2
            ),
            np.array((0, 0)),
            dtype=np.int32
        )

        for (src, target, positive, negative, total) in extracted_evidence:
            i = self.users_idx(src)
            j = self.users_idx(target)
            initial_evidence[i, j] = np.array((positive, negative))
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
        # print("worldview", worldview)

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

        # print(evidence - initial_evidence)

        # fig, ax = plt.subplots()
        # ax.matshow(evidence[:,:,0], cmap=plt.cm.Blues)

        # plt.savefig(f'networks/evidence.pos.png')

        # fig, ax = plt.subplots()
        # ax.matshow(evidence[:,:,1], cmap=plt.cm.Blues)
        
        # plt.savefig(f'networks/evidence.neg.png')

        # for (src, target, positive, negative, total) in evidence:
        #     i = user_idxs.index(src)
        #     j = user_idxs.index(target)

        #     reputations[i, j] = to_opinion(positive, negative, total)

        self.R = worldview
        self.E = evidence


    # Get the reputation opinions of every user in the system from a's perspective
    def perspective(self, a):
        return self.R[self.users_idx(a)]
    
    # Gets b's reputation from a's perspective
    def reputation_of(self, a, b):
        return self.R[self.users_idx(a), self.users_idx(a)]




class VisualisedEBSLReputationEngine(ReputationEngine):
    def __init__(self, interactions):
        self.algo_logs = []
        def algo_log(x):
            self.algo_logs.append(x)

        users = interactions.get_users()
        self.users_idx = ListToMatrixIndexMapper(users)
        
        shape = (
            len(users),
            len(users),
            3
        )

        # 
        # 1. Convert interactions to evidence (aggregation)
        # 
        extracted_evidence = interactions.get_evidence()
    

        # 
        # 2. Convert evidence to opinions and build reputations matrix.
        # 
        reputations = np.full(
            shape, 
            U,
            dtype=np.float64
        )

        initial_evidence = np.full(
            (
                len(users),
                len(users),
                2
            ),
            np.array((0, 0)),
            dtype=np.int32
        )

        for (src, target, positive, negative, total) in extracted_evidence:
            i = self.users_idx(src)
            j = self.users_idx(target)
            initial_evidence[i, j] = np.array((positive, negative))
            reputations[i, j] = to_opinion(positive, negative, total)
        
        # 
        # 3. Converge opinions matrix.
        # 
        algo_log("START {} {}".format(len(users), len(users)))

        configure_ebsl(reputations)
        direct_opinions = np.copy(reputations)
        worldview = optimize.fixed_point(
            build_f_R_hooked(algo_log), 
            reputations, 
            args=(direct_opinions,), 
            method="iteration",
            # xtol=1e-5
        )
        algo_log("END")

        # print("worldview", worldview)

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

        self.R = worldview
        self.E = evidence

        print(self.algo_logs)

    # Get the reputation opinions of every user in the system from a's perspective
    def perspective(self, a):
        return self.R[self.users_idx(a)]
    
    # Gets b's reputation from a's perspective
    def reputation_of(self, a, b):
        return self.R[self.users_idx(a), self.users_idx(a)]

