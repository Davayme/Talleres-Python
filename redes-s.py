#redes semanticas 20-03-2025
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from([('mamifero', 'animal'), ('gato', 'mamifero'), ('perro', 'mamifero')])

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2500, node_color='orange', font_size=20, font_color='black', font_weight='bold', edge_color='blue', width=3, style='dashed')
plt.show()