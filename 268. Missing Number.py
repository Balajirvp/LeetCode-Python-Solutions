# Solution 1 (228 ms, 16.4 MB)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = range(len(nums)+1)
        return list(set(arr) - set(nums))[0]

# Solution 2 (202 ms, 15.1 MB)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        exp_sum = n*(n+1)/2
        act_sum = sum(nums)
        return int(exp_sum - act_sum)