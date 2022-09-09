# Solution 1 (39 ms, 13.8 MB)

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        return min(Counter(s)[i] // Counter(target)[i] for i in target)
        