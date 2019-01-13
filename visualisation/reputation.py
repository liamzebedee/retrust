
import numpy as np

from ebsl.lib import *
from retrust.reputation import ReputationEngine
from ebsl.helpers import ListToMatrixIndexMapper

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from matplotlib.animation import FFMpegWriter


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import six
import io

import random


from shared import matplotlib_helpers

import gc
def build_f_R_hooked(hook):
    def f_R_hooked(x, A):
        R = np.copy(x)

        # square
        assert(R.shape[0] == R.shape[1])

        for (i, j) in np.ndindex(R.shape[0], R.shape[1]):
            hook("JUDGE", (i, j), R)
            g = np.copy(A[i,j])
            
            for k in range(R.shape[0]):
                g = opinion_add(
                    g, 
                    opinion_mult(R[i,k], A[k,j])
                )

                hook("MULT", (i, k, k, j), R)

            # R[i,j] = opinion_add(g, opinion(0.1, 0, 0.9))
            # R[i,j] = opinion_scalar_mult(.7, g)
            R[i,j] = g

        
        # fill diagonal
        for i in np.ndindex(R.shape[0]):
            R[i,i] = U
    
        
        hook("ITERATION", None, R)

        return R
    
    return f_R_hooked


converge_i = 0
node_perspective = 0
node_judged = 0
class VisualisedEBSLReputationEngine(ReputationEngine):
    def __init__(self, interactions):
        self.algo_logs = []
        def algo_log(a,b,c):
            self.algo_logs.append((a,b,c))
        
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

        # setup animation
        ims = []

        def setup_plt(dataframe, col_width=3.0, row_height=0.625, 
                            row_color="w", edge_color="black", 
                            ax=None, highlight_color="mediumpurple",
                            highlights=[], **kwargs):
            if ax is None:
                size = (np.array(dataframe.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
                fig, ax = plt.subplots(figsize=size)
                ax.axis('off')

            return fig, ax

        # width = 8
        # data_np = np.zeros(shape=(4,4))
        data = None
        table = None
        def get_dataframe(nparr=reputations, bbox=[0, 0, 1, 1], font_size=14,):
            data = pd.DataFrame.from_records(nparr)
            table = ax.table(cellText=data.values, bbox=bbox)

            table.auto_set_font_size(False)
            table.set_fontsize(font_size)

            return table
        
        # buf = io.BytesIO()

        # def save_frame():
        #     fig.savefig(buf, format='svg')
        #     ims.append([
        #         # fig
        #         # fig.savefig(buf, format='svg')
                
        #     ])

        fig, ax = setup_plt(pd.DataFrame.from_records(reputations))
        
        # im = plt.show(fig)
        # save_frame()


        configure_ebsl(reputations)
        direct_opinions = np.copy(reputations)
        worldview = optimize.fixed_point(
            build_f_R_hooked(algo_log), 
            reputations, 
            args=(direct_opinions,), 
            method="iteration",
            # xtol=1e-5
        )

        # now animate everything that happened
        
        def updatefig(idx):
            global converge_i, node_perspective, node_judged
            ax.clear()

            # for idx, log in enumerate(self.algo_logs):
            print(float(idx / len(self.algo_logs)) * 100, len(self.algo_logs))
            action, data, new_R = self.algo_logs[idx]

            mpl_table = get_dataframe(new_R)
            # mpl_table = table
 
            for k, cell in six.iteritems(mpl_table._cells):
                cell.set_facecolor('w')
            
            if action == 'ITERATION':
                converge_i += 1
            elif action == 'JUDGE':
                node_perspective, node_judged = data
            elif action == 'MULT':
                i, j, k, l = data
                if i == l and j == k:
                    mpl_table._cells[i,j].set_facecolor('hotpink')
                else:
                    mpl_table._cells[i,j].set_facecolor('lightpink')
                    mpl_table._cells[k,l].set_facecolor('lightpink')

            mpl_table._cells[node_perspective,node_judged].set_facecolor('lightblue')

            ax.set_title('Reputation matrix')
            t = plt.text(0, 0, '\n'.join([
                'Convergence round {}'.format(converge_i),
                'Current node perspective - {}'.format(node_perspective),
                'Examining node - {}'.format(node_judged)
            ]), bbox={'facecolor':'white'})
            

            return [ax]


        # ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
        #                         repeat_delay=1000)
        # writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
        # ani.save("movie.mp4", writer=writer)
        anim = animation.FuncAnimation(fig, updatefig, len(self.algo_logs), blit=True, save_count=1)
        # anim.save("test.mp4", fps=60)
        plt.show()


        # evidence = np.full(
        #     (
        #         len(users),
        #         len(users),
        #         2
        #     ),
        #     np.array((0, 0)),
        #     dtype=np.int32
        # )

        # for (i, j) in np.ndindex(worldview.shape[0], worldview.shape[1]):
        #     evidence[i,j] = to_evidence(worldview[i,j])

        # self.R = worldview
        # self.E = evidence


    # Get the reputation opinions of every user in the system from a's perspective
    def perspective(self, a):
        return self.R[self.users_idx(a)]
    
    # Gets b's reputation from a's perspective
    def reputation_of(self, a, b):
        return self.R[self.users_idx(a), self.users_idx(a)]

