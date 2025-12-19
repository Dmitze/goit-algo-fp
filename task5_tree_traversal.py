import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


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


def dfs_visualization(root):
    colors_map = {}
    step = 0
    stack = [root]
    
    while stack:
        node = stack.pop()
        step += 1
        intensity = int((step / 10) * 255)
        colors_map[node.id] = f'#{intensity:02x}{intensity:02x}{255:02x}'
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return colors_map


def bfs_visualization(root):
    colors_map = {}
    step = 0
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        step += 1
        intensity = int((step / 10) * 255)
        colors_map[node.id] = f'#{intensity:02x}{intensity:02x}{255:02x}'
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return colors_map


def apply_colors(root, colors_map):
    def apply(node):
        if node:
            node.color = colors_map.get(node.id, "skyblue")
            apply(node.left)
            apply(node.right)
    
    apply(root)


def draw_tree(tree_root, title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title(title)
    plt.show()


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    dfs_colors = dfs_visualization(root)
    apply_colors(root, dfs_colors)
    draw_tree(root, "DFS - Пошук у глибину")

    bfs_colors = bfs_visualization(root)
    apply_colors(root, bfs_colors)
    draw_tree(root, "BFS - Пошук у ширину")
