# Solution 1 (31 ms, 13.8 MB)

class Solution:
    def minTimeToType(self, word: str) -> int:
        l = len(word)
        val = abs(ord(word[0]) - ord('a'))
        if val > 13:
            val = 26 - val
        for i in range(1, len(word)):
            val1 = abs(ord(word[i]) - ord(word[i-1]))
            if val1 > 13:
                val1 = 26 - val1
            val+=val1
        return val + l