# Solution 1 (157 ms, 15.2 MB)

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        arr = [i for i, val in enumerate(s) if val == c]
        arr1 = [[]*len(arr) for i in range(len(s))]
        for i in range(len(s)):
            for j in arr:
                arr1[i].append(abs(j-i))
        return [min(i) for i in arr1]

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
                
        