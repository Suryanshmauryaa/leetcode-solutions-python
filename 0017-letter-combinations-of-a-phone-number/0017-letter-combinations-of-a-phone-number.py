class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
            
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        res = []
        
        def backtrack(index: int, current_string: str):
            if index == len(digits):
                res.append(current_string)
                return
                
            current_digit = digits[index]
            letters = phone_map[current_digit]
            
            for letter in letters:
                backtrack(index + 1, current_string + letter)
                
        backtrack(0, "")
        
        return res