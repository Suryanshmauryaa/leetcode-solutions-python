import collections
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        adj = [[] for _ in range(n)]
        in_degree = [0] * n
        
        unique_weights = set()
        
        for u, v, w in edges:
            if online[u] and online[v]:
                adj[u].append((v, w))
                in_degree[v] += 1
                unique_weights.add(w)
                
        if not unique_weights:
            return -1
            
        unique_weights = sorted(list(unique_weights))
        
        queue = collections.deque()
        for i in range(n):
            if online[i] and in_degree[i] == 0:
                queue.append(i)
                
        top_order = []
        while queue:
            u = queue.popleft()
            top_order.append(u)
            for v, w in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
                    
        def check(M: int) -> bool:
            dist = [float('inf')] * n
            dist[0] = 0
            
            for u in top_order:
                d_u = dist[u]
                if d_u == float('inf'):
                    continue
                
                for v, w in adj[u]:
                    if w >= M and d_u + w < dist[v]:
                        dist[v] = d_u + w
                        
            return dist[n - 1] <= k

        ans = -1
        L = 0
        R = len(unique_weights) - 1
        
        while L <= R:
            mid = (L + R) // 2
            if check(unique_weights[mid]):
                ans = unique_weights[mid]
                L = mid + 1     
            else:
                R = mid - 1      
                
        return ans