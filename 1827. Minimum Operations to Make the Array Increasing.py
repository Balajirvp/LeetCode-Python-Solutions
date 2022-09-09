# Solution 1 (141 ms, 14.6 MB)

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                continue
            else:
                count+= (nums[i] - nums[i+1] + 1)
                nums[i+1] = nums[i] + 1
        return count