# Solution 1 (54 ms, 14 MB)

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if len(str(nums[i])) % 2 == 0:
                count+=1
        return count

# Solution 2 (53 ms, 13.9 MB)

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        arr = [1 for i in nums if len(str(i)) % 2 == 0]
        return len(arr)


