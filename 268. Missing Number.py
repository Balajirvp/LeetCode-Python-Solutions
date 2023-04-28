# Solution 1 (131 ms, 18.7 MB)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = range(len(nums)+1)
        return list(set(arr) - set(nums))[0]

# Solution 2 (151 ms, 17.8 MB)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        exp_sum = n*(n+1)/2
        act_sum = sum(nums)
        return int(exp_sum - act_sum)

# Solution 3 (153 ms, 17.7 MB)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for idx, val in enumerate(nums):
            if idx != val:
                return idx
        return len(nums)
        