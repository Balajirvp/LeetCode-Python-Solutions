# Solution 1 (58 ms, 15.1 MB)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            arr = zip(sorted(s), sorted(t))
            for i in arr:
                if i[0] != i[1]:
                    return False
            return True
        return False
    
# Solution 2 (31 ms, 14.4 MB)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            letter = 'abcdefghijklmnopqrstuvwxyz'
            for i in letter:
                if s.count(i) != t.count(i):
                    return False
            return True
        return False
    
# Solution 3 (45 ms, 14.4 MB)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        
        for i in s:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        
        for j in t:
            if j in dict1:
                dict1[j]-=1
            else:
                dict1[j]=1
        
        if set(dict1.values()) == set((0,)):
            return True
        return False
