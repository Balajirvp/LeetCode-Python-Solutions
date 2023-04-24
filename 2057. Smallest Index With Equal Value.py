# Solution 1 (88 ms, 13.8 MB)

class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        arr = [idx for idx, val in enumerate(nums) if idx % 10 == val]
        if arr:
            return arr[0]
        return -1

# Solution 2 (89 ms, 13.9 MB)

class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for idx, val in enumerate(nums):
            if idx % 10 == val:
                return idx
        return -1