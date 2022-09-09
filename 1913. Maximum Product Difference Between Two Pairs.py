# Solution 1 (307 ms, 15.2 MB)

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1]*nums[-2] - nums[0]*nums[1]