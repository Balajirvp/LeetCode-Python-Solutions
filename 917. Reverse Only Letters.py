# Solution 1 (35 ms, 13.9 MB)

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [i for i in s if (ord(i) > 64 and ord(i) < 91) or (ord(i) > 96 and ord(i) < 123)][::-1]
        idx = {i:v for i,v in enumerate(s) if (ord(v) > 32 and ord(v) < 65) or (ord(v) > 90 and ord(v) < 97)}
        for i,v in idx.items():
             letters.insert(i, v)
        return ''.join(letters)
