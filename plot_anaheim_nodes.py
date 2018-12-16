# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 01:08:08 2018

@author: rajar
"""

import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

datafolder = Path("Transportation-Networks-Data/Anaheim")
file_to_open = datafolder / "Anaheim_edge_list.txt"

graph = nx.read_edgelist(file_to_open)

# Top centrality nodes in the network un-weighted
nodes = ['317', '330', '355', '333', '329', '299']

nodes_2 =  ['321', '266', '303', '305', '358', '315', '357', '356', 
            '388', '327', '343', '316', ]

nx.draw_spectral(graph, node_size = 1)
pos = nx.spectral_layout(graph)
nx.draw_networkx_nodes(graph,pos,nodelist = nodes,node_color='b',
                       node_size=200, alpha=0.9)
plt.savefig("Transportation-Networks-Data/Anaheim/Anaheim_top_cent_unweighted", 
            dpi = 400)
plt.axis('off')
plt.show()


# Top degree centrality nodes un-weighted
nodes_degree = ['330', '303', '337', '299', '317', '266', '267',
                '269', '273', '302', '304', '308', '341', '329',
                '332', '333', '361', '369', '385', '373']

nx.draw_spectral(graph, node_size = 1)
pos = nx.spectral_layout(graph)
nx.draw_networkx_nodes(graph,pos,nodelist = nodes_degree,node_color='b',
                       node_size=200, alpha=0.9)
plt.savefig("Transportation-Networks-Data/Anaheim/Anaheim_top_degree_unweighted", 
            dpi = 400)
plt.axis('off')
plt.show()