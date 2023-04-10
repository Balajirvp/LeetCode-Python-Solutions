# Solution 1 (59 ms, 14.1 MB)

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        num = original
        while num in nums:
            num = num*2
        return num