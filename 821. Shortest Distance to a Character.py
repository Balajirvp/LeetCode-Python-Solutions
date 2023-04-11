# Solution 1 (69 ms, 13.9 MB)     

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        idxs = [idx for idx, val in enumerate(s) if val == c]
        arr = []
        for i, v in enumerate(s):
            arr.append(min([abs(idx - i) for idx in idxs]))
        return arr

# Solution 2 (57 ms, 13.9 MB)

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        arr = [0]*len(s)
        for i in range(len(s)):
            if s[i] == c:
                arr[i] = 0
            elif i == 0:
                arr[i] = s.index(c)
            elif i == len(s) - 1:
                arr[i] = s[::-1].index(c)
            else:
                a = s[i::-1].index(c) if c in s[i::-1] else float(inf)
                b = s[i::].index(c) if c in s[i::] else float(inf)
                arr[i] = min(a, b)
        return arr