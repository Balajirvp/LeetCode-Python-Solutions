# Solution 1 (855 ms, 26 MB)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums):
            return True
        return False

# Solution 2 (520 ms, 26 MB)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if sorted(list(set(nums))) != sorted(nums):
            return True
        return False