import networkx as nx
from data import data

import matplotlib.pyplot as plt

G = nx.Graph()

for d in data:
    G.add_node(d)

for d in data:
    for o in data[d]['connected']:
        G.add_edge(d,o)

nx.draw(G, with_labels=True, font_weight='bold')

plt.show()