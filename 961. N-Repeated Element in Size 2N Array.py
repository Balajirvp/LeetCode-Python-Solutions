# Solution 1 (212 ms, 15.5 MB)

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)/2
        arr = Counter(nums)
        return [i for i, v in arr.items() if v == n][0]

# Solution 2 (202 ms, 15.2 MB)

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                return i
            else:
                d[i] = 0