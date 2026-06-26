from itertools import accumulate

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        M = r - l + 1

        if n == 1:
            return M % MOD
        if n == 2:
            return (M * (M - 1)) % MOD

        dp_down = [M - 1 - v for v in range(M)]
        dp_up = [v for v in range(M)]
        
        for _ in range(3, n + 1):
            pref_down = list(accumulate(dp_down))
            pref_up = list(accumulate(dp_up))
            total_up = pref_up[-1]
            new_dp_up = [0] + [pref_down[v - 1] % MOD for v in range(1, M)]
            new_dp_down = [(total_up - pref_up[v]) % MOD for v in range(M)]
            
            dp_down = new_dp_down
            dp_up = new_dp_up
            
        return (sum(dp_down) + sum(dp_up)) % MOD