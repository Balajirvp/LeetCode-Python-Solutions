# Solution 1 (32 ms, 13.9 MB)

class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = { '(':')', '[':']', '{':'}'  }
        arr = []
        if len(s) % 2:
            return False
        else:
            for i in s:
                if i in dict1:
                    arr.append(dict1[i])
                elif len(arr) == 0 or arr.pop() != i:
                    return False
            return len(arr) == 0
                    
# Solution 2 (47 ms, 13.9 MB)

class Solution:
    def isValid(self, s: str) -> bool:
        while len(s) > 0:
            l = len(s)
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
            if l == len(s): return False
        return True
                    
