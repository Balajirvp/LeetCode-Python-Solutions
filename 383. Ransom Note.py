# Solution 1 (123 ms, 14 MB)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return len(Counter(ransomNote) - Counter(magazine)) == 0