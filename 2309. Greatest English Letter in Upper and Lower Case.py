# Solution 1 (52 ms, 14 MB)

class Solution:
    def greatestLetter(self, s: str) -> str:
        upp = [i for i in list(s) if i.isupper() == True]
        low = [i.upper() for i in list(s) if i.islower() == True]
        comm = set(upp) & set(low)
        if len(comm):
            return max(comm)
        else:
            return ''

# Solution 2 (33 ms, 13.8 MB)

class Solution:
    def greatestLetter(self, s: str) -> str:
        arr = []
        for i in range(26):
            if chr(97 + i) in s and chr(65 + i) in s:
                arr.append(chr(65 + i))
        if len(arr) == 0:
            return ""
        return max(arr)
