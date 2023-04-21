# Solution 1 (28 ms, 13.9 MB)

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        a = Counter(word1)
        b = Counter(word2)
        for idx, val in a.items():
            if abs(b[idx] - val) > 3:
                return False
            else:
                continue
        for idx, val in b.items():
            if abs(a[idx] - val) > 3:
                return False
            else:
                continue
        return True