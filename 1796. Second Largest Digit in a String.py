# Solution 1 (50 ms, 13.7 MB)

class Solution:
    def secondHighest(self, s: str) -> int:
        nums = [int(i) for i in s if i.isnumeric()]
        res = sorted(set(nums), reverse = True)
        if len(res) > 1:
            return res[1]
        else:
            return -1