# Solution 1 (121 ms, 14.1 MB)

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(len(words)):
            if words[i] == words[i][::-1]:
                return words[i]
                break
        return ""