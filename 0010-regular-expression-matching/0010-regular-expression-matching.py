class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        
        def dfs(i: int, j: int) -> bool:
            if (i, j) in memo:
                return memo[(i, j)]
            
            if j >= len(p):
                return i >= len(s)
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            if j + 1 < len(p) and p[j+1] == '*':
                memo[(i, j)] = (dfs(i, j + 2) or (match and dfs(i + 1, j)))
            else:
                memo[(i, j)] = match and dfs(i + 1, j + 1)
                
            return memo[(i, j)]
        
        return dfs(0, 0)