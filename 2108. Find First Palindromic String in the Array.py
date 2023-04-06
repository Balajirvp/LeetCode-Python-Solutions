# Solution 1 (69 ms, 13.9 MB)

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            if i == i[::-1]:
                return i
        return ""