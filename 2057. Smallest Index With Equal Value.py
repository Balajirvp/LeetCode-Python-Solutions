# Solution 1 (97 ms, 13.9 MB)

class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        arr = [i for i in range(len(nums)) if i % 10 == nums[i]]
        if arr:
            return min(arr)
        else: return -1

