from typing import List

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return 0
            
        S = [0] * (n + 1)
        for i in range(n):
            S[i + 1] = S[i] + nums[i]
            
        # inc_left[i]: start index of the strictly increasing sequence ending at i
        inc_left = [i for i in range(n)]
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                inc_left[i] = inc_left[i-1]
                
        # inc_right[i]: end index of the strictly increasing sequence starting at i
        inc_right = [i for i in range(n)]
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                inc_right[i] = inc_right[i+1]
        
        # Precompute f(p): min S[l] for l in [inc_left[p], p-1]
        f = [float('inf')] * n
        for p in range(1, n-2):
            # p must be a peak: nums[p-1] < nums[p] > nums[p+1]
            if nums[p-1] < nums[p] and nums[p] > nums[p+1]:
                # l can range from inc_left[p] to p-1
                if inc_left[p] <= p - 1:
                    f[p] = min(S[inc_left[p] : p])
        
        # Precompute g(q): max S[r+1] for r in [q+1, inc_right[q]]
        # which is max S[k] for k in [q+2, inc_right[q]+1]
        g = [-float('inf')] * n
        for q in range(2, n-1):
            # q must be a valley: nums[q-1] > nums[q] < nums[q+1]
            if nums[q-1] > nums[q] and nums[q] < nums[q+1]:
                # r can range from q+1 to inc_right[q]
                # S[r+1] can range from S[q+2] to S[inc_right[q]+1]
                if q + 1 <= inc_right[q]:
                    g[q] = max(S[q+2 : inc_right[q] + 2])
        
        unique_nums = sorted(list(set(nums)))
        rank = {val: i + 1 for i, val in enumerate(unique_nums)}
        K = len(unique_nums)
        
        # Fenwick Tree for suffix max query
        # Maximize g(q) - f(p) where nums[p] > nums[q]
        # Equivalent to f(p) + g(q) where nums[p] > nums[q]
        bit = [-float('inf')] * (K + 1)
        
        def update(idx, val):
            idx = K - idx + 1
            while idx <= K:
                bit[idx] = max(bit[idx], val)
                idx += idx & (-idx)
                
        def query(idx):
            idx = K - idx
            res = -float('inf')
            while idx > 0:
                res = max(res, bit[idx])
                idx -= idx & (-idx)
            return res
            
        max_trionic_sum = -float('inf')
        
        for q in range(2, n-1):
            # Potential p is q-1
            p = q - 1
            if p >= 1 and f[p] != float('inf'):
                update(rank[nums[p]], f[p])
                
            if g[q] != -float('inf'):
                # Query BIT for p such that rank(nums[p]) > rank(nums[q])
                res = query(rank[nums[q]])
                if res != -float('inf'):
                    max_trionic_sum = max(max_trionic_sum, g[q] - res)
                    
        return int(max_trionic_sum)