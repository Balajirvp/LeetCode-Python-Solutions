# Time limit exceeded 18/22 cases passed

from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        res = 1
        for idx, val in enumerate(nums):
            nums1 = nums[:]
            nums1.pop(idx)
            arr.append(nums1)        
        return [prod(i) for i in arr]
    
# Solution 1 (264 ms  22.4 MB)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0]*len(nums)
        right = [0]*len(nums)

        left[0] = right[-1] = 1
        res = []

        for i in range(1, len(nums)):
            left[i] = left[i - 1]*nums[i - 1]
            right[len(nums) - i - 1] = right[len(nums) - i]*nums[len(nums) - i]

        for i in range(len(nums)):
            res.append(left[i]*right[i])
        
        return res