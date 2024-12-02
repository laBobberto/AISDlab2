import networkx as nx
from networkx.drawing.nx_pydot import write_dot
import pydot
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, left = None, right = None, color = None):
        self.left = left
        self.right = right
        self.key = key
        self.label = str(key)
        self.color = color # В данном случае будет использоваться только в Красно-черном дереве, в остальных деревьях будет равно None всегда



def drawNodes(root):
    def addNode(node, parent=None, path=''):
        if node is None:
            return
        node_id = f"{node.key}_{path}"
        G.add_node(node_id, label=node.label, color=node.color)
        if parent:
            parent_id = f"{parent.key}_{path[:-1]}"
            G.add_edge(parent_id, node_id)
        addNode(node.left, node, path + 'L')
        addNode(node.right, node, path + 'R')

    G = nx.DiGraph()
    addNode(root)
    pos = nx.nx_pydot.graphviz_layout(G, prog='dot')

    # Извлекаем метки и цвета узлов
    labels = nx.get_node_attributes(G, 'label')
    colors = nx.get_node_attributes(G, 'color')
    node_colors = [colors.get(node, 'lightblue') if colors.get(node) else 'blue' for node in G.nodes]

    nx.draw(
        G, pos, labels=labels, with_labels=True,
        font_size=10, font_family='sans-serif', node_size=600,
        node_color=node_colors, font_color='white'
    )
    plt.show()





