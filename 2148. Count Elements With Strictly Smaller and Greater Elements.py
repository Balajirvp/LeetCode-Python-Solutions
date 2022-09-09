# Solution 1 (58 ms, 13.9 MB)

class Solution:
    def countElements(self, nums: List[int]) -> int:
        a = sorted(set(nums))
        b = a[1:len(a) - 1]
        return sum(1 for i in nums if i in b)
        