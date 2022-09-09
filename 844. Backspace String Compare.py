# Solution 1 (59 ms, 14 MB)  

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        s = list(s)
        t = list(t)
        while i < len(s):
            if i > 0 and s[i] == '#':
                s.pop(i-1)
                s.pop(i-1)
                i = 0
            elif i == 0 and s[i] == '#':
                s.pop(i)
                i = 0
            else:
                i+=1
        while j < len(t):
            if j > 0 and t[j] == '#':
                t.pop(j-1)
                t.pop(j-1)
                j = 0
            elif j == 0 and t[j] == '#':
                t.pop(j)
                j = 0
            else:
                j+=1 
        return s == t

# Solution 1 (38 ms, 13.9 MB)  

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s):
            s = list(s)
            i = 0
            while i < len(s):
                if i > 0 and s[i] == '#':
                    s.pop(i-1)
                    s.pop(i-1)
                    i = 0
                elif i == 0 and s[i] == '#':
                    s.pop(i)
                    i = 0
                else:
                    i+=1
            return s
        return build(s) == build(t)