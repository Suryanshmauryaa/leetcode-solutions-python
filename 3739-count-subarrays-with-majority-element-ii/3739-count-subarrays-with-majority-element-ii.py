class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        bit = [0] * (2 * n + 3)
        
        def add(idx: int, val: int):
            while idx < len(bit):
                bit[idx] += val
                idx += idx & (-idx)
                
        def query(idx: int) -> int:
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s
            
        current_sum = 0
        ans = 0
        offset = n + 2
        
        add(0 + offset, 1)
        
        for num in nums:
            if num == target:
                current_sum += 1
            else:
                current_sum -= 1
                
            ans += query((current_sum - 1) + offset)
            
            add(current_sum + offset, 1)
            
        return ans