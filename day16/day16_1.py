import networkx as nx
from data import data

import matplotlib.pyplot as plt

import itertools

nodes = len(data)

max_depth = 30

G = nx.Graph()

for d in set(data):
    G.add_node(d)

for d in data:
    for o in data[d]['connected']:
        G.add_edge(d, o, weight=1)

shortestPaths = dict(nx.shortest_path_length(G))
# Reduce graph
nodes_to_remove = []
for n in G:
    if data[n]['rate']:
        continue
    # Delete node and add new edges
    for a, b in itertools.combinations(G.neighbors(n), 2):
        G.add_edge(a, b, weight=G.edges[n, a]
                   ['weight']+G.edges[n, b]['weight'])
    nodes_to_remove.append(n)

G.remove_nodes_from(nodes_to_remove)

bit_index = {x: 1 << i for i, x in enumerate(sorted(G))}


def search(node, time, state, score, lut):
    lut[state] = max(score, lut.get(state,0))

    for n in bit_index:
        if bit_index[n] & state:
            continue

        new_time = time - shortestPaths[node][n] -1

        if new_time <= 0:
            continue

        new_score = score + new_time * data[n]['rate']
        new_state = state | bit_index[n]
        
        search(n, new_time, new_state, new_score, lut)
    return lut

print(shortestPaths)
rtn = search('AA', 30, 0, 0, {})
from pprint import pprint
pprint(rtn)
print(max(rtn.values()))

dg = G.to_directed()


pos = nx.spring_layout(dg)
nx.draw(dg, pos, with_labels=True, font_weight='bold')
labels = nx.get_edge_attributes(dg, 'weight')
nx.draw_networkx_edge_labels(dg, pos, edge_labels=labels)

plt.show()
