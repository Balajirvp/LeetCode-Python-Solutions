# Solution 1 (96 ms, 14.2 MB)

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums

# Solution 2 (86 ms, 14.2 MB)

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

# can use chain, list unloading