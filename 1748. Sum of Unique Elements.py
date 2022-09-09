# Solution 1 (49 ms, 13.9 MB)

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        nums1 = [i for i in nums if nums.count(i) == 1]
        return sum(nums1)