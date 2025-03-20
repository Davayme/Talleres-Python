import networkx as nx
import matplotlib.pyplot as plt
# Crear grafo
G = nx.DiGraph()

# Agregar nodos con atributos
G.add_node("Ana Garcia", tipo="Estudiante", edad=15)
G.add_node("Juan Perez", tipo="Profesor", departamento="Matematicas")
G.add_node("Matematicas", tipo="Materia", creditos=4)
G.add_node("Examen Parcial 1", tipo="Evaluacion", fecha="2021-10-01")
G.add_node("90", tipo="Calificacion")
G.add_node("Boletin 1", tipo="Boletin")

# Agregar aristas relaciones
G.add_edge("Ana Garcia", "Matematicas", relacion="inscrito en")
G.add_edge("Juan Perez", "Matematicas", relacion="ensña")
G.add_edge("Matematicas", "Examen Parcial 1", relacion="Evaluado por")
G.add_edge("Ana Garcia", "90", relacion="Obtuvo")
G.add_edge("Examen Parcial 1", "90", relacion="resultado")
G.add_edge("Ana Garcia", "Boletin 1", relacion="recibio")
G.add_edge("90", "Boletin 1", relacion="Incluido en")

# Dibujar grafo
plt.figure(figsize=(7, 5))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray', font_size=6)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'relacion'), font_color='red', font_size=6)
plt.show()