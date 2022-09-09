# Solution 1 (83 ms, 13.9 MB)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] - 1)*(nums[-2]-1)