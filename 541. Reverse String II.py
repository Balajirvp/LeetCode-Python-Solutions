# Solution 1 (43 ms, 14 MB)

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2*k):
            if i == 0:
                s[i:i+k] = s[i+k-1::-1]
            else:
                s[i:i+k] = s[i+k-1:i-1:-1]
        return ''.join(s)