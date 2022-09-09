# Solution 1 (46 ms, 15.6 MB)

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [i for i in s if i in 'aeiouAEIOU'][::-1]
        s = list(s)
        j = 0
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                s[i] = vowels[j]
                j+=1
        return ''.join(s)