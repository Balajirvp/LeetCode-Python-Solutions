# Solution 1 (68 ms, 13.7 MB)

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        while sum(nums) > 0:
            val = min([i for i in nums if i > 0])
            nums = [i - val for i in nums if i > 0]
            cnt+=1
        return cnt
        