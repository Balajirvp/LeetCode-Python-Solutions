# Solution 1 (32 ms, 13.9 MB)

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower())