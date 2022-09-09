# Solution 1 (47 ms  13.9 MB)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split()
        return len(a[-1])