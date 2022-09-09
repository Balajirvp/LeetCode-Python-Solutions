# Solution 1 (43 ms, 13.9 MB)

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for i in patterns:
            if i in word:
                count+=1
        return count