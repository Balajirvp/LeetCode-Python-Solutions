# Solution 1 (116 ms, 14 MB)

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        l = len(nums)
        i = 0
        while i < l:
            if original == nums[i]:
                original = (original*2)
                i = 0
            else:
                i+=1
        return original

# Solution 2 (62 ms, 14.2 MB)

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        a = [i for i in nums if i % original == 0]
        i = 0
        l = len(a)
        while i < l:
            if original == a[i]:
                original = original*2
                i = 0
            else:
                i+=1
        return original