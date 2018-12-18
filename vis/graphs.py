import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout, to_agraph
from networkx.drawing.nx_agraph import read_dot, write_dot

from pygraphviz import *

import os
import json


import numpy as np

from interactions import InteractionsEngine

def file_without_ext(fname):
    return os.path.splitext(os.path.basename(fname))[0]


class graph():
    def __init__(self, path, worldview_algo):
        self.path = path
        self.name = file_without_ext(path)
        self.interactions = InteractionsEngine()

        # reads .interactions
        with open(path, 'r') as f:
            interactions_list = []
            for line in f.read().split('\n'):
                if line == '':
                    continue
            
                interactions_list.append([
                    int(i) for i in line.split(' ')
                ])

            self.interactions.insert(interactions_list)

            # self.G = self.interactions_list_to_graphs(self.interactions)
                
        self.opinions, self.evidence = worldview_algo(self.interactions)

        # with open(f'networks/{self.name}.evidence.json', 'w') as f:
        #     json.dump(self.evidence, f) 
        # with open(f'networks/{self.name}.opinions.json', 'w') as f:
        #     json.dump(self.opinions, f)
        

        np.set_printoptions(precision=3)
        print(self.opinions)

        # self.render_trust(self.evidence, self.interactions, self.G)
        # self.render_dot(self.G, self.G)
        # self.render_heatmap(self.G)
    
    def interactions_list_to_graphs(self, interactions):
        G = nx.MultiDiGraph()
        for from_, to, _ in interactions:
            G.add_edge(from_, to)
        
        return G, interactions
    
    
    def render_trust(self, evidence, interactions, G):
        pos = nx.spring_layout(G)

        for i, node_view in enumerate(self.evidence):
            node_id = i
            
            # evidence
            # colour nodes by the amount of evidence they have
            evidence_totals = []
            for j, other in enumerate(self.evidence[i]):
                posit, negat = self.evidence[i][j]
                total = posit - negat
                evidence_totals.append(total)
            
            # RdYlBu
            # cmap = plt.get_cmap('RdYlBu')
            cmap = plt.get_cmap('RdBu_r')
            node_color = evidence_totals
            print(G.nodes())
            print(node_color)

            plt.figure()
            nodes = nx.draw_networkx_nodes(
                G, 
                pos=pos,
                node_size=250,
                cmap=cmap, 
                node_color=node_color, 
                # nodelist=list(measures.keys())
            )
            
            labels = nx.draw_networkx_labels(G, pos, font_color='white')
            edges = nx.draw_networkx_edges(G, pos)

            plt.title(f"Evidence map for node {node_id}")
            plt.colorbar(nodes)
            plt.axis('off')
            # plt.show()
            plt.savefig(f'networks/{self.name}.{node_id}.evidence.png')

    def render_dot(self, G, AGraph):
        to_agraph(G).draw(
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
            # print(list(measures.keys()), list(measures.values()))
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

        plt.figure()
        pos = nx.spring_layout(G)
        draw(G, pos, nx.degree_centrality(G), 'Degree Centrality')

