# Solution 1 (65 ms, 13.9 MB)

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        else:
            arr = len([i for i in nums if i < 0])
            if arr % 2 == 0:
                return 1
            else:
                return -1

# Solution 2 (66 ms, 14 MB)

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        val = 1
        for i in nums:
            val = val*i
        if val > 0:
            return 1
        elif val < 0:
            return -1
        else:
            return 0