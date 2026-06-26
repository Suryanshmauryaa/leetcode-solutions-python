class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        M = r - l + 1
        
        if n == 1:
            return M % MOD
        if n == 2:
            return (M * (M - 1)) % MOD
            
        size = 2 * M

        V0 = [0] * size
        for v in range(M):
            V0[v] = v                  
            V0[v + M] = M - 1 - v      
            
        T = [[0] * size for _ in range(size)]
        for u in range(M):
            for v in range(u):
                T[u][v + M] = 1
            
            for v in range(u + 1, M):
                T[u + M][v] = 1
                
        def multiply(A, B):
            C = [[0] * size for _ in range(size)]
            for i in range(size):
                for k in range(size):
                    if A[i][k]:  
                        val = A[i][k]
                        rowB = B[k]
                        rowC = C[i]
                        for j in range(size):
                            rowC[j] = (rowC[j] + val * rowB[j]) % MOD
            return C

        def multiply_vec(V, B):
            res = [0] * size
            for k in range(size):
                if V[k]:
                    val = V[k]
                    rowB = B[k]
                    for j in range(size):
                        res[j] = (res[j] + val * rowB[j]) % MOD
            return res

        res = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
        base = T
        p = n - 2
        
        while p > 0:
            if p % 2 == 1:
                res = multiply(res, base)
            base = multiply(base, base)
            p //= 2
            
        V_final = multiply_vec(V0, res)
        
        return sum(V_final) % MOD