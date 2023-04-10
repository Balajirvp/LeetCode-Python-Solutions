# Solution 1 (88 ms, 14.1 MB)

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        arr = Counter(nums)
        return sum([val % 2 for idx, val in arr.items()]) == 0