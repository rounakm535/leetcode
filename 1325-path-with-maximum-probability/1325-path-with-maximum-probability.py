import heapq
from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Create an adjacency list to represent the graph
        graph = defaultdict(list)
        for (a, b), prob in zip(edges, succProb):
            graph[a].append((b, prob))
            graph[b].append((a, prob))
        
        # Initialize the max-heap with the start node
        max_heap = [(-1, start_node)]
        visited = set()
        
        while max_heap:
            prob, node = heapq.heappop(max_heap)
            prob = -prob  # Convert back to positive probability
            
            if node == end_node:
                return prob
            
            if node in visited:
                continue
            
            visited.add(node)
            
            for neighbor, edge_prob in graph[node]:
                if neighbor not in visited:
                    new_prob = prob * edge_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))
        
        return 0.0