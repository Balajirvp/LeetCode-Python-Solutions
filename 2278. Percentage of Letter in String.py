# Solution 1 (31 ms, 13.8 MB)

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        cnt = sum([1 for i in s if i == letter])
        return floor((cnt*100)/len(s))

# Solution 2 (31 ms, 13.7 MB)

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return floor((s.count(letter)*100)/len(s))