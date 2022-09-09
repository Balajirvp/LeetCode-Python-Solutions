# Solution 1 (38 ms, 13.8 MB)

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1 = set('qwertyuiop')
        r2 = set('asdfghjkl')
        r3 = set('zxcvbnm')
        arr = []
        for i in words:
            if len(set(i.lower()) & r1) == len(set(i.lower())) or len(set(i.lower()) & r2) == len(set(i.lower())) or len(set(i.lower()) & r3) == len(set(i.lower())):
                arr.append(i)
        return arr