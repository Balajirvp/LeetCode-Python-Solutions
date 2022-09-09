# Solution 1 (36 ms, 13.9 MB)

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        a = list(text.split())
        b = set(list(brokenLetters))
        count = 0
        for i in a:
            if len(set(list(i)) & b) == 0:
                count+=1
        return count