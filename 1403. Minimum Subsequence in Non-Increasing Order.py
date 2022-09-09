# Solution 1 (111 ms, 13.9 MB)

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        i = 1
        for j in range(len(nums)):
            if sum(nums[-1:-1-i:-1]) > sum(nums[0:-i]):
                return nums[-1:-1-i:-1]
            else:
                i+=1
                continue
        
    