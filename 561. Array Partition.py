# Solution 1 (283 ms, 16.7 MB)

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        arr = sorted(nums)
        return sum([min(arr[i:i+2]) for i in range(0, len(arr), 2)])

# Solution 2 (262 ms, 16.9 MB)

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])