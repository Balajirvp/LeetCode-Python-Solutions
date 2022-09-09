# Solution 1 (36 ms, 13.8 MB)

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        l = len(s)
        v = sum(1 for i in list(s) if i == letter)
        return math.floor((v*100)/l)