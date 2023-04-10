# Solution 1 (75 ms, 14.3 MB)

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(j) for i in nums for j in str(i)]
