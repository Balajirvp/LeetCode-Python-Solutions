# Solution 1 (49 ms  13.9 MB)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        b = [i for i in nums if i != val]
        length = len(b)
        for i in range(length):
            nums[i] = b[i]
        return length