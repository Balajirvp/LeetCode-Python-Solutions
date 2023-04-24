# Solution 1 (5993 ms, 16.8 MB)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:       
        for i in range(len(nums)):
           if nums.count(nums[i]) == 1:
              return nums[i]


# Solution 2 (131 ms, 16.6 MB)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return [i for i,val in Counter(nums).items() if val == 1][0]
