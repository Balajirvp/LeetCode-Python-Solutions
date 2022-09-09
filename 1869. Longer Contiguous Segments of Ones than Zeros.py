# Solution 1 (684 ms, 14.2 MB)

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        seg1 = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s) + 1) if set(s[i:j]) == {'1'}]
        seg0 = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s) + 1) if set(s[i:j]) == {'0'}]
        if seg1 and seg0:
            return len(max(seg1)) > len(max(seg0))
        elif seg1:
            return True
        else:
            return False