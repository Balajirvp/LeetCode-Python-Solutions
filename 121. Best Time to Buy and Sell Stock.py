
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

# Final Solution (916 ms, 24.9 MB)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = float('inf')
        diff = 0

        for i in prices:
            if i < minn:
                minn = i
            elif i - minn > diff:
                diff = i - minn
        return diff
