class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        half_len = (m + n + 1) // 2
        
        while left <= right:
            i = (left + right) // 2
            j = half_len - i
            
            max_left_A = float('-inf') if i == 0 else nums1[i - 1]
            min_right_A = float('inf') if i == m else nums1[i]
            
            max_left_B = float('-inf') if j == 0 else nums2[j - 1]
            min_right_B = float('inf') if j == n else nums2[j]
            
            if max_left_A <= min_right_B and max_left_B <= min_right_A:
                if (m + n) % 2 == 1:
                    return float(max(max_left_A, max_left_B))
                return (max(max_left_A, max_left_B) + min(min_right_A, min_right_B)) / 2.0
                
            elif max_left_A > min_right_B:
                right = i - 1
            else:
                left = i + 1
                
        raise ValueError("Input arrays are not sorted or invalid.")