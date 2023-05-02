# Solution 1 (69 ms, 16.7 MB)

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = len(arr)
        nums = range(1, l + k + 1)
        final = set(nums) - set(arr)
        return sorted(final)[k-1]