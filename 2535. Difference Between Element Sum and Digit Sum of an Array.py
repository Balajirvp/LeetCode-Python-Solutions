# Solution 1 (137 ms, 14.1 MB)

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return abs(sum(nums) - sum([int(j) for i in nums for j in str(i)]))
