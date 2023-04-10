# Solution 1 (29 ms, 13.9 MB)

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        arr = text.split()
        cnt = 0
        for i in arr:
            if len(set(i) & set(brokenLetters)) == 0:
                cnt+=1
        return cnt

