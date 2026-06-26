class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2147483647 
        
        result = 0
        
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        while x != 0:
            pop = x % 10
            x //= 10
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and pop > 7):
                return 0
            
            result = (result * 10) + pop
            
        return sign * result