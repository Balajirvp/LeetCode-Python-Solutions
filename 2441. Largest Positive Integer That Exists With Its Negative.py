# Solution 1 (126 ms, 14.2 MB)

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        neg = [-i for i in nums if i < 0]
        pos = [i for i in nums if i > 0]
        val = set(neg) & set(pos)
        if val:
            return max(val)
        return -1
         