# Solution 1 (172 ms, 17.8 MB)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = [i for i in nums if i != 0]
        zeros = nums.count(0)
        nums[:] = arr + zeros*[0]

# Solution 2 (165 ms, 18 MB)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = [i for i in nums if i != 0] + [i for i in nums if i == 0]
