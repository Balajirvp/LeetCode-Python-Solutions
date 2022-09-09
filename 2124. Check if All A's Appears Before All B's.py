# Solution 1 (32 ms, 13.8 MB)

class Solution:
    def checkString(self, s: str) -> bool:
        a = [idx for idx, val in enumerate(s) if val == 'a']
        b = [idx for idx, val in enumerate(s) if val == 'b']
        if len(a) == 0 or len(b) == 0:
            return True
        else:
            return max(a) < min(b)
        