import matplotlib as mpl
mpl.use('TkAgg')

import networkx as nx


# G = to_networkx_graph(pgv.AGraph(graphdot_code))

# G = nx.generators.social.karate_club_graph()
# G = nx.Graph()




def parse_edgelist(data):
    G = nx.MultiDiGraph()
    edges = list(
        filter(lambda x: len(x) > 1, map(lambda x: x.strip().split(' '), data.strip().split('\n')))
    )
    G.add_edges_from(edges)
#   for edge in edges:
#     G.add_edge(*edge)
    return G
  
  
social_network_1 = parse_edgelist("""
1 2

2 1

3 1

3 4

4 5


5 4
""")

G = social_network_1







import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
# for Notebook
# %matplotlib inline

from networkx.drawing.nx_agraph import graphviz_layout

plt.figure(1)

pos = graphviz_layout(G)
nx.draw(G, pos=pos, node_size=1600, cmap=plt.cm.Blues,
#         node_color=range(len(G)),
        prog='dot')
labels = nx.draw_networkx_labels(G, pos, font_color='black')
plt.title('Trust network')
plt.savefig('network-structure.png')
# plt.show()


import numpy as np


# Taken from
# https://aksakalli.github.io/2017/07/17/network-centrality-measures-and-their-visualization.html
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
    plt.savefig('heatmap.png')

plt.figure(2)
pos = nx.spring_layout(G)
draw(G, pos, nx.degree_centrality(G), 'Degree Centrality')