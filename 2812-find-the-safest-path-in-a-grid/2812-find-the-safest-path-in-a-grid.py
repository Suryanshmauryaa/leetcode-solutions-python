import heapq
from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        q = deque()
        dist = [[float('inf')] * n for _ in range(n)]
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c))
                    dist[r][c] = 0
                    
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == float('inf'):
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
                    
        pq = [(-dist[0][0], 0, 0)] 
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        
        while pq:
            safe, r, c = heapq.heappop(pq)
            safe = -safe 
            
            if r == n - 1 and c == n - 1:
                return safe
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    next_safe = min(safe, dist[nr][nc])
                    heapq.heappush(pq, (-next_safe, nr, nc))
                    
        return 0