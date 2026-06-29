class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        max_cost = max(costs)
        
        freq = [0] * (max_cost + 1)
        for cost in costs:
            freq[cost] += 1
            
        ice_creams_bought = 0
        
        for cost in range(1, max_cost + 1):
            if freq[cost] > 0:
                if coins < cost:
                    break
                    
                can_buy = min(freq[cost], coins // cost)
                
                ice_creams_bought += can_buy
                coins -= cost * can_buy
                
        return ice_creams_bought