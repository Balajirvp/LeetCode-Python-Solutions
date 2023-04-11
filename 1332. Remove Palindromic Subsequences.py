# Solution 1 (30 ms, 13.9 MB)

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == s[::-1]:
            return 1
        else:
            return len(set(s))