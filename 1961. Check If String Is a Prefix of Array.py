# Solution 1 (49 ms, 13.8 MB)

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        i = 0
        a = ''
        while i < len(words):
            a = a + words[i]
            if a == s:
                return True
                break
            i+=1
        return False