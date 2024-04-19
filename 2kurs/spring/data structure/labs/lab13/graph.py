import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes. In NetworkX, edges can be added before nodes.
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('B', 'D')
G.add_edge('C', 'D')
G.add_edge('D', 'A')
G.add_edge('A', 'C')

# You can also add nodes and edges using lists
# Adding multiple edges
edges = [('E', 'F'), ('F', 'G'), ('G', 'E')]
G.add_edges_from(edges)

# Adding single nodes: 
G.add_node('H')
G.add_edge('H','A')

# Draw the graph
nx.draw(G, with_labels=True, node_color='skyblue', node_size=700, edge_color='#909090', font_size=10, font_weight='bold', arrows=True)

# Show plot
plt.show()