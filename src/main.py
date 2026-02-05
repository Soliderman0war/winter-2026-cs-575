import networkx as nx

def getG():
    G = nx.DiGraph()
    G.add_nodes_from([1,2,3,4,5,6])
    G.add_edges_from([(1,2),(2,3),(3,4),(4,5),(4,1),(5,6),(6,5)])
    pos = nx.nx_pydot.graphviz_layout(G,prog='neato')
    return G, pos

G_cycle, _ = getG()

eig_centrality = nx.eigenvector_centrality(G_cycle, max_iter=1000)
print("\nEigenvector Centrality (NetworkX):")
print("=" * 40)
for node in sorted(eig_centrality.keys()):
    print(f"Node {node}: {eig_centrality[node]:.2f}")