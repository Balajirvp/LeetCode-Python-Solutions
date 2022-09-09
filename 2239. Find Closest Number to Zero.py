# Solution 1 (216 ms, 14.2 MB)

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        a = {i:abs(i) for i in nums}
        val = min(a.values())
        b = [k for k,v in a.items() if v == val]
        return max(b)