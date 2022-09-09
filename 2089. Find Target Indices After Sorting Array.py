# Solution 1 (55 ms, 13.7 MB)

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        arr = []
        for i in range(len(nums)):
            if nums[i] == target:
                arr.append(i)
        return arr