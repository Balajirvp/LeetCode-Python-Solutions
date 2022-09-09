# Solution 1 (6322 ms	16.7 MB)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
           if nums.count(nums[i]) == 1:
              return nums[i]


# Solution 2 (To be added)