# Solution 1 (51 ms, 14 MB)

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        arr = list(s.split())
        nums = [int(i) for i in arr if i.isnumeric()]
        res = []
        for i in range(1, len(nums)):
            res.append(nums[i] - nums[i - 1])
        result = [i for i in res if i <= 0]
        if len(result) >= 1:
            return False
        else:
            return True