# Solution 1 (110 ms, 15.2 MB)

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [num for num in set(nums) if nums.count(num) > len(nums) / 3]