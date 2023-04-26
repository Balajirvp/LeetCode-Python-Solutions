# Solution 1 (62 ms, 16.3 MB)

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        arr = []
        while nums:
            if len(nums) >= 2:
                arr.append(str(nums[0]) + str(nums[-1]))
                nums.pop(0)
                nums.pop()
            else:
                arr.append(str(nums[0]))
                nums.pop()
        return sum(int(i) for i in arr)