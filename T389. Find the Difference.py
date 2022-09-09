# Solution 1 (42 ms, 13.8 MB)

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s1 = Counter(s)
        t1 = Counter(t)
        res = list(t1 - s1)
        return res[0]
        