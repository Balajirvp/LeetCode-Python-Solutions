# Solution 1 (50 ms, 13.9 MB)

class Solution:
    def removeVowels(self, s: str) -> str:
        return ''.join([i for i in list(s) if i not in 'aeiou'])

# Solution 2 (25 ms, 13.9 MB)

class Solution:
    def removeVowels(self, s: str) -> str:
        return ''.join([i for i in s if i not in 'aeiou'])