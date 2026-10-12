
from typing import List, Dict

class Solution:
    def shortestPath(
        self, n: int, edges: List[List[int]], src: int
    ) -> Dict[int, int]:

        # 1. Build adjacency list
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        # 2. Initialize distances and visited
        distances = [float("inf")] * n
        visited = [False] * n

        distances[src] = 0

        # 3. Process vertices
        for _ in range(n):
            node = -1

            # Find the unvisited vertex with minimum distance
            for i in range(n):
                if not visited[i]:
                    if node == -1 or distances[i] < distances[node]:
                        node = i

            # Stop if remaining vertices are unreachable
            if node == -1 or distances[node] == float("inf"):
                break

            visited[node] = True

            # 4. Relax outgoing edges
            for neighbor, weight in graph[node]:
                new_distance = distances[node] + weight

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

        result: Dict[int, int] = {}


        for i in range(n):
            if distances[i] == float("inf"):
                result[i] = -1
            else:
                result[i] = int(distances[i])

        return result