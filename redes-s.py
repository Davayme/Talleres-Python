import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

#Agregar nodos de profesiones y habilidades
profesiones = ["Ingeniero", "Doctor", "Programador", "Cientifico de Datos"] 
habilidades = ["Matematicas", "Programacion", "Analisis de Datos", "Medicina"]

G.add_nodes_from(profesiones, color='blue')
G.add_nodes_from(habilidades, color='green')

#Agregar las relaciones 

G.add_edges_from([("Ingeniero", "Matematicas"), 
                  ("Programador", "Programacion"), 
                  ("Cientifico de Datos", "Analisis de Datos"),
                  ("Doctor", "Medicina"),
                  #("Doctor", "Analisis de Datos"),
                  ("Cientifico de Datos", "Programacion"),
                  #("Cientifico de Datos", "Matematicas"),
                  ("Ingeniero", "Analisis de Datos"), ])

#Dibujar el grafo
plt.figure(figsize=(7, 5))
nx.draw(G, with_labels=True, node_color="lightblue", edge_color='gray', node_size=2500, font_size=9)

plt.show()