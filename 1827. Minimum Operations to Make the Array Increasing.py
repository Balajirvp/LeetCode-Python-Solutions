# Solution 1 (140 ms, 14.6 MB)

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

# Solution 2 (126 ms, 14.7 MB)

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        else:
            cnt = 0
            for i in range(1, len(nums)):
                if nums[i] > nums[i - 1]:
                    continue
                else:
                    cnt+= nums[i - 1] + 1 - nums[i] 
                    nums[i] = nums[i - 1] + 1
            return cnt