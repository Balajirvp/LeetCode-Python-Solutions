# Solution 1 (198 ms, 14.1 MB)

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            val = nums[nums[i]]
            arr.append(val)
        return arr

# Solution 2 (179 ms, 14.2 MB)

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]
        
