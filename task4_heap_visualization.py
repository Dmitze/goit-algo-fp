import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def heap_to_tree(heap_list):
    if not heap_list:
        return None

    nodes = {i: Node(heap_list[i]) for i in range(len(heap_list))}

    for i in range(len(heap_list)):
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2

        if left_idx < len(heap_list):
            nodes[i].left = nodes[left_idx]
        if right_idx < len(heap_list):
            nodes[i].right = nodes[right_idx]

    return nodes[0]


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)


def draw_heap(heap_list):
    root = heap_to_tree(heap_list)
    
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(tree, root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title("Бінарна купа")
    plt.show()


if __name__ == "__main__":
    heap_list = [10, 20, 15, 30, 40, 50, 25]
    
    print("Heap array:", heap_list)
    draw_heap(heap_list)
