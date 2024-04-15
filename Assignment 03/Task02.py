import networkx as nx
import random

dG = nx.DiGraph()
dG.add_nodes_from(["A","B","C","D","E","F","G"])
dG.add_edges_from([("C", "A", {"weight": 2}), ("E", "A", {"weight": 3}), ("G", "A", {"weight": 6}), ("F", "B", {"weight": 1}), ("B", "B", {"weight": 8}), ("A", "C", {"weight": 9}), ("G", "C", {"weight": 12}), ("F", "C", {"weight": 11}), ("E", "D", {"weight": 10}), ("A", "E", {"weight": 9}), ("D", "E", {"weight": 1}), ("B", "F", {"weight": 5}), ("G", "F", {"weight": 13}), ("C", "F", {"weight": 3}), ("A", "G", {"weight": 9}), ("C", "G", {"weight": 8}), ("F", "G", {"weight": 3})])
    
edge_labels = nx.get_edge_attributes(dG, 'weight')
nx.draw_networkx_edge_labels(dG, pos=nx.circular_layout(dG), edge_labels=edge_labels)


shortest_path = nx.shortest_path(dG, source="A", target="B", weight="weight")
shortest_path_length = nx.shortest_path_length(dG, source="A", target="B", weight="weight")

node_colors = ['skyblue' if node not in shortest_path else 'red' for node in dG.nodes]

nx.draw(dG, with_labels=True,pos=nx.circular_layout(dG),node_color=node_colors)

print("Shortest Path from A to B:", shortest_path)
print("Length of Shortest Path:", shortest_path_length)