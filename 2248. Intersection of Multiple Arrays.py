# Solution 1 (69 ms, 14.3 MB)

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        for i in range(len(nums)-1):
            nums[i+1] = set(nums[i]) & set(nums[i+1])
        return sorted(nums[-1])

# Solution 2 (69 ms, 14.3 MB)

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        l = len(nums)
        return sorted([idx for idx, val in Counter([j for i in nums for j in i]).items() if val == l])
        