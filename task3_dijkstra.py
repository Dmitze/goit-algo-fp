import heapq
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.nodes = set()

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))
        self.nodes.add(u)
        self.nodes.add(v)

    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.nodes}
        distances[start] = 0
        
        parents = {node: None for node in self.nodes}
        heap = [(0, start)]

        while heap:
            current_dist, current_node = heapq.heappop(heap)

            if current_dist > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                distance = current_dist + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    parents[neighbor] = current_node
                    heapq.heappush(heap, (distance, neighbor))

        return distances, parents

    def get_path(self, parents, start, end):
        path = []
        current = end

        while current is not None:
            path.append(current)
            current = parents[current]

        path.reverse()
        return path if path[0] == start else []


if __name__ == "__main__":
    g = Graph()
    
    edges = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'E', 10),
        ('D', 'E', 2)
    ]
    
    for u, v, w in edges:
        g.add_edge(u, v, w)

    distances, parents = g.dijkstra('A')

    print("Найкоротші відстані від А:")
    for node, dist in sorted(distances.items()):
        print(f"  до {node}: {dist}")

    print("\nМаршрути:")
    for node in sorted(distances.keys()):
        if node != 'A':
            path = g.get_path(parents, 'A', node)
            print(f"  A → {node}: {' → '.join(path)}")
