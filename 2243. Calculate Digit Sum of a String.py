# Solution 1 (32 ms, 13.9 MB)

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            arr = [s[i:i+k] for i in range(0, len(s), k)]
            s = ''.join([str(sum([int(j) for j in i])) for i in arr])
        return s