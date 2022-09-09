# Solution 1 (58 ms, 14.1 MB)

class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr) + 1
        s = (n*(arr[0] + arr[-1]))/2
        return int(s) - sum(arr)
        