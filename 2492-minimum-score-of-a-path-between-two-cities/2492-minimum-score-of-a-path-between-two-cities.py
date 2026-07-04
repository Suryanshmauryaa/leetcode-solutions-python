from collections import deque
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
      
        adj = [[] for _ in range(n + 1)]
        for u, v, distance in roads:
            adj[u].append((v, distance))
            adj[v].append((u, distance))
            
        visited = set()
        queue = deque([1])
        visited.add(1)
        
        min_score = float('inf')
        
        while queue:
            node = queue.popleft()
            
            for neighbor, distance in adj[node]:
                min_score = min(min_score, distance)
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score