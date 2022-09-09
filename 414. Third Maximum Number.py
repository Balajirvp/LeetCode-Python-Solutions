# Solution 1 (58 ms, 15.6 MB)

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a = sorted(list(set(nums))) 
        if len(a) >= 3:
            return a[-3]
        else:
            return a[-1]

