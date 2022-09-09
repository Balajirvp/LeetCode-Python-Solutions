# Solution 1 (77 ms, 14 MB)

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        a = [num for num in set(nums) if nums.count(num) > len(nums)/ 2]
        if len(a) > 0:
            return a[0] == target
        return False