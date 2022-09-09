# Solution 1 (48 ms, 13.8 MB)

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.islower() or word.isupper() or word.capitalize() == word:
            return True
        else:
            return False

# Solution 2 (55 ms, 13.8 MB)

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return re.fullmatch(r'[A-Z]*|.[a-z]*', word)