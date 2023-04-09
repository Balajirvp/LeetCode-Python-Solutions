# Solution 1 (32 ms, 13.9 MB)

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum([1 for i in words if i[:len(pref)] == pref ])