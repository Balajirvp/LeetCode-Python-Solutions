# Solution 1 (62 ms, 14.4 MB)

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        for i in range(len(nums)-1):
            nums[i+1] = set(nums[i]) & set(nums[i+1])
        return sorted(nums[-1])