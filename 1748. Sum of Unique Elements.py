# Solution 1 (30 ms, 13.9 MB)

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        nums1 = [i for i in nums if nums.count(i) == 1]
        return sum(nums1)

# Solution 2 (31 ms, 13.8 MB)    

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        arr = Counter(nums)
        return sum([idx for idx, val in arr.items() if val == 1])