from collections import deque
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = grid[0][0]
        
        q = deque([(grid[0][0], 0, 0)])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while q:
            cost, r, c = q.popleft()
            
            if r == m - 1 and c == n - 1:
                return cost < health
                
            if cost > dist[r][c]:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    ncost = cost + grid[nr][nc]
                    
                    if ncost < dist[nr][nc]:
                        dist[nr][nc] = ncost
                        if grid[nr][nc] == 0:
                            q.appendleft((ncost, nr, nc))
                        else:
                            q.append((ncost, nr, nc))
                            
        return False