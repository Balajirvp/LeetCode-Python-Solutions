# Solution 1 (87 ms  14.9 MB)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target > nums[-1]:
                return len(nums)
            elif target > nums[i]:
                continue
            else:
                return i

# Solution 2 (50 ms  14.7 MB) (Binary search)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            elif target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return left
        