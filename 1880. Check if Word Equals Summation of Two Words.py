# Solution 1 (31 ms, 13.7 MB)

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        word1 = ''.join([str(ord(i) - 97) for i in firstWord])
        word2 = ''.join([str(ord(i) - 97) for i in secondWord])
        target = ''.join([str(ord(i) - 97) for i in targetWord])
        return int(word1) + int(word2) == int(target)
