# Solution 1 (53 ms, 14 MB)

class Solution:
    def greatestLetter(self, s: str) -> str:
        upp = [i for i in list(s) if i.isupper() == True]
        low = [i.upper() for i in list(s) if i.islower() == True]
        comm = set(upp) & set(low)
        if len(comm):
            return max(comm)
        else:
            return ''