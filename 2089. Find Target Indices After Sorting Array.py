# Solution 1 (43 ms, 13.8 MB)

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        return [idx for idx, val in enumerate(sorted(nums)) if val == target]