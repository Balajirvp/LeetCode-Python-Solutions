# Solution 1 (66 ms, 13.8 MB)

from itertools import accumulate

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        val = list(accumulate(nums))
        return max(1-min(val),1)

# Solution 2 (46 ms, 13.9 MB)

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        a = [sum(nums[0:0+i]) for i in range(1,len(nums)+1)]
        return (max(1-min(a),1))
