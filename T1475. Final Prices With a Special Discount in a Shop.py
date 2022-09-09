# Solution 1 (71 ms, 14.1 MB)

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    prices[i]-= prices[j]
                    break
                else:
                    continue
        return prices

