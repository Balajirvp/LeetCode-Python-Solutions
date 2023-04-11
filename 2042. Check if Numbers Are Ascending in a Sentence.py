# Solution 1 (27 ms, 13.9 MB)

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = [int(i) for i in s.split() if i.isdigit()]
        arr = []
        for i in range(0, len(nums) - 1):
            arr.append(nums[i+1] - nums[i])
        return sum([1 for i in arr if i <= 0]) == 0