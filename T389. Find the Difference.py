# Solution 1 (30 ms, 13.9 MB)

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s1 = Counter(s)
        t1 = Counter(t)
        res = list(t1 - s1)
        return res[0]

# Solution 2 (36 ms, 14 MB)

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a1 = sorted(s)
        a2 = sorted(t)
        for i in range(len(a1)):
            if a1[i] == a2[i]:
                continue
            else:
                return a2[i]
        return a2[-1]