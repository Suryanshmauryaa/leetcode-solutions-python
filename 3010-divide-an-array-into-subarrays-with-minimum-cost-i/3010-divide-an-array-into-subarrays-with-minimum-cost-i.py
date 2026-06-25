class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        sorted_tail = sorted(nums[1:])
        
        return nums[0] + sorted_tail[0] + sorted_tail[1]