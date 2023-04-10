# Solution 1 (222 ms, 14.3 MB)

class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        arr = []
        for idx, val in enumerate(nums):
            left = sum(nums[:idx])
            right = sum(nums[idx + 1:])
            arr.append(abs(left - right))
        return arr