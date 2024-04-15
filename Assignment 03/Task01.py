import networkx as nx

dG = nx.DiGraph()
dG.add_nodes_from(["A","B","C","D","E","F","G"])
dG.add_edges_from([("C", "A"), ("E", "A"), ("G", "A"),("F", "B"), ("B", "B"),("A", "C"), ("G", "C"),("F", "C"), ("E", "D"),("A", "E"), ("D", "E"),("B", "F"), ("G", "F"),("C", "F"),("A", "G"), ("C", "G"),("F", "G")])
print("Loops in graph:", list(nx.selfloop_edges(dG)))
nx.draw(dG, with_labels=True)