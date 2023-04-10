# Solution 1 (36 ms, 13.9 MB)

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        arr = Counter(nums)
        a = sum([val // 2 for idx, val in arr.items()])
        b = sum([val % 2 for idx, val in arr.items()])
        return [a,b]