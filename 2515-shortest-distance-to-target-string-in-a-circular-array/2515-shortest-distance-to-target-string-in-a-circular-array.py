class Solution:
    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_dist = float('inf')
        
        for i, word in enumerate(words):
            if word == target:

                dist = abs(i - startIndex)
                
                circular_dist = n - dist
                
                min_dist = min(min_dist, dist, circular_dist)
                
        return min_dist if min_dist != float('inf') else -1