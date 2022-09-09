
# My Initial Solution (Time limit exceeded) (Not scalable at all)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        left, right = 0, len(prices) - 1

        while left < right:
            while left < right:
                if prices[right] > prices[left] and prices[right] - prices[left] > maxx:
                    maxx = prices[right] - prices[left]
                left+= 1
                continue

            right-= 1
            left = 0
            
        return maxx

# Easier version of the above code (Time limit exceeded) (Not scalable at all)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        
        for i in range(len(prices) - 1):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > maxx:
                    maxx = profit
        
        return maxx

# Final Solution (1816 ms, 25 MB)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        
        return max_profit