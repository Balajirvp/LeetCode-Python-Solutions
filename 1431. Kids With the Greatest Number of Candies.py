# Solution 1 (65 ms, 13.8 MB)

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [candies[i]+extraCandies >= max(candies) for i in range(len(candies))]