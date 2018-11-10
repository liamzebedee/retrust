import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
from networkx.drawing.nx_agraph import read_dot

from pygraphviz import *

import os

def file_without_ext(fname):
    return os.path.splitext(os.path.basename(fname))[0]

class graph():
    def __init__(self, path):
        self.path = path
        self.name = file_without_ext(path)
        with open(path, 'r') as f:
            self.G = read_dot(f)
            self.AGraph = AGraph(path)
            # print(self.G.edges())
        self.render_dot(self.G, self.AGraph)
        self.render_heatmap(self.G)

    def interactions_list_to_graphs(self):
        

    def render_dot(self, G, AGraph):
        AGraph.draw(
            f'networks/{self.name}.network-structure.png',
            format='png',
            prog='dot'
        )
        # plt.figure()

        # pos = graphviz_layout(G)
        # nx.draw(G, pos=pos, node_size=1600, cmap=plt.cm.Blues,
        # #         node_color=range(len(G)),
        #         prog='dot')
        # labels = nx.draw_networkx_labels(G, pos, font_color='black')
        # plt.title('Trust network')
        # plt.savefig(f'networks/{self.name}.network-structure.png')

    def render_heatmap(self, G):
        def draw(G, pos, measures, measure_name):
            print(list(measures.keys()), list(measures.values()))
            nodes = nx.draw_networkx_nodes(G, pos, node_size=250, cmap=plt.cm.plasma, 
                                        node_color=list(measures.values()),
                                        nodelist=list(measures.keys())  
                                        )
            nodes.set_norm(mcolors.SymLogNorm(linthresh=0.01, linscale=1))
            
            labels = nx.draw_networkx_labels(G, pos, font_color='white')
            edges = nx.draw_networkx_edges(G, pos)

            plt.title(measure_name)
            plt.colorbar(nodes)
            plt.axis('off')
            # plt.show()
            plt.savefig(f'networks/{self.name}.heatmap.png')

        plt.figure(2)
        pos = nx.spring_layout(G)
        draw(G, pos, nx.degree_centrality(G), 'Degree Centrality')

