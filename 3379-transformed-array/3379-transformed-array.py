class Solution:
    def constructTransformedArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        
        for i in range(n):
            landing_index = (i + nums[i]) % n
            result[i] = nums[landing_index]
            
        return result