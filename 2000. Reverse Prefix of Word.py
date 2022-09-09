# Solution 1 (28 ms, 13.9 MB)

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            i = word.index(ch)
            return word[i::-1] + word[i+1:]
        else:
            return word