class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT = 2147483647  
        MIN_INT = -2147483648 
        
        n = len(s)
        i = 0
        
        while i < n and s[i] == ' ':
            i += 1
            
        if i == n:
            return 0
            
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            if result > MAX_INT // 10 or (result == MAX_INT // 10 and digit > 7):
                return MAX_INT if sign == 1 else MIN_INT
                
            result = (result * 10) + digit
            i += 1
            
        return sign * result