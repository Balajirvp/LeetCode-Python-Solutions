# Solution 1 (1457 ms, 16.3 MB)

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        max_candies = len(candyType)/2
        type_candies = len(set(candyType))
        return int(min(max_candies, type_candies))