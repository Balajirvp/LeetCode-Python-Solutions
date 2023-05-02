# Solution 1 (351 ms, 17.4 MB)

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        arr = [str(i) for i in nums]
        val = ''.join(arr).split('0')
        return max(len(i) for i in val)