class Solution:
    def isTrionic(self, nums: list[int]) -> bool:
        n = len(nums)
        
        if n < 4:
            return False
            
        p = 0
        
        while p + 1 < n and nums[p] < nums[p + 1]:
            p += 1
            
        if p == 0 or p >= n - 2:
            return False
            
        q = p
        
        while q + 1 < n and nums[q] > nums[q + 1]:
            q += 1
            
        if q == p or q >= n - 1:
            return False
            
        r = q
        while r + 1 < n and nums[r] < nums[r + 1]:
            r += 1
            
        return r == n - 1