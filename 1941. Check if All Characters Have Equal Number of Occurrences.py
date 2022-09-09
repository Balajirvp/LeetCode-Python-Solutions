# Solution 1 (41 ms, 14 MB)

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        a = Counter(s)
        return len(set(a.values())) == 1