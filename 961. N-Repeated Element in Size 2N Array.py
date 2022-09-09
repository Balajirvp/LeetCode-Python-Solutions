
# Time limit exceeded solution

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = int(len(nums)/2)
        a = [i for i in nums if nums.count(i) == n]
        return a[0]

# Solution 1 (359 ms, 15.8 MB)

from collections import Counter

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = int(len(nums)/2)
        a = dict(Counter(nums))
        b = [k for k,v in a.items() if v == n]
        return b[0]

# Solution 1 (212 ms, 15.2 MB)

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                return i
            else:
                d[i] = 0