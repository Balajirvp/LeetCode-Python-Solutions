# Solution 1 (35 ms, 14 MB)

class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        minn = min(nums)
        arr = [i for i in str(minn)]
        summ = sum([int(i) for i in arr])
        return int(summ % 2 == 0)

# Solution 2 (30 ms, 13.7 MB)

class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        nums.sort()
        arr = [i for i in str(nums[0])]
        summ = sum([int(i) for i in arr])
        return int(summ % 2 == 0)