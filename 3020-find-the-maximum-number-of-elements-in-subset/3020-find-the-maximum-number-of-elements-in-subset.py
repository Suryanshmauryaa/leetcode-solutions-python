from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counts = Counter(nums)
        max_length = 1
        
        if 1 in counts:
            ones = counts[1]
            if ones % 2 == 0:
                ones -= 1
            max_length = max(max_length, ones)
            
        for x in counts:
            if x == 1:
                continue
                
            curr_len = 0
            curr = x
            
            while counts[curr] > 1:
                curr_len += 2
                curr *= curr
                
            if counts[curr] > 0:
                curr_len += 1   
            else:
                curr_len -= 1   

            max_length = max(max_length, curr_len)
            
        return max_length