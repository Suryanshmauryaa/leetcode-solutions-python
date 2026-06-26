class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        result_chars = []
        
        for word in words:
            word_weight = 0
            for char in word:
                char_idx = ord(char) - ord('a')
                word_weight += weights[char_idx]
            
            remainder = word_weight % 26

            mapped_char = chr(ord('z') - remainder)
            result_chars.append(mapped_char)
            
        return "".join(result_chars)