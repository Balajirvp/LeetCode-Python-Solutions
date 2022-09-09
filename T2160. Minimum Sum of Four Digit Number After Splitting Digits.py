# Solution 1 (40 ms, 13.9 MB)

class Solution:
    def minimumSum(self, num: int) -> int:
        nums = [i for i in str(num)]
        nums.sort()
        a = nums[0] + nums[2]
        b = nums[1] + nums[3]
        return int(a) + int(b)