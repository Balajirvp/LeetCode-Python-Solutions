# Solution 1 (104 ms, 32.2 MB)

import numpy as np

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return np.cumsum(nums)

# Solution 2 (34 ms, 14.1 MB)

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            if i == 0:
                arr.append(nums[i])
            else:
                arr.append(nums[i]+arr[-1])
        return arr
   
# Solution 3 (54 ms, 14 MB)

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[:i+1]) for i in range(len(nums))]
