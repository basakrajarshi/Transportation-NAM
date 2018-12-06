# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 01:33:24 2018

@author: rajar
"""

import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

datafolder = Path("Transportation-Networks-Data/Philadelphia")
file_to_open = datafolder / "Philadelphia-net.txt"

#file = open(file_to_open)
#next(file)


#for line in file:
#    print(line)

#file_to_write = open("Transportation-Networks-Data/Philadelphia/Philadelphia_edge_list.txt", "w")
#
#nodes = {}
#count = 1
#for line_a in file:
#    k = line_a.strip().split('\t')
##    print(k)
#    file_to_write.write(k[0] + '\t' + k[1] + '\n')
#    
#file_to_write.close()
#file.close()

new_file = datafolder / "Philadelphia_edge_list.txt"

graph = nx.read_edgelist(new_file)

nx.draw_circular(graph, node_size = 1)
plt.savefig("Transportation-Networks-Data/Philadelphia/Philadelphia_draw_circular", dpi = 400)
plt.show()

nx.draw_kamada_kawai(graph, node_size = 1)
plt.savefig("Transportation-Networks-Data/Philadelphia/Philadelphia_draw_kamada_kawai", dpi = 400)
plt.show()

nx.draw_random(graph, node_size = 1)
plt.savefig("Transportation-Networks-Data/Philadelphia/Philadelphia_draw_random", dpi = 400)
plt.show()

nx.draw_spectral(graph, node_size = 1)
plt.savefig("Transportation-Networks-Data/Philadelphia/Philadelphia_draw_spectral", dpi = 400)
plt.show()

nx.draw_spring(graph, node_size = 1)
plt.savefig("Transportation-Networks-Data/Philadelphia/Philadelphia_draw_spring", dpi = 400)
plt.show()

nx.draw_shell(graph, node_size = 1)
plt.savefig("Transportation-Networks-Data/Philadelphia/Philadelphia_draw_shell", dpi = 400)
plt.show()

print(len(graph.nodes()))
print(len(graph.edges()))