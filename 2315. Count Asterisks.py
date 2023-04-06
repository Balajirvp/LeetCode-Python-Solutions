# Solution 1 (35 ms, 13.9 MB)

class Solution:
    def countAsterisks(self, s: str) -> int:
        idx = [i for i,v in enumerate(s) if v == '|']
        count = 0
        l = len(idx)
        i = 1
        j = 2
        if idx:
            while i < l and j < l:
                count+=s[idx[i]+1:idx[j]].count('*')
                i+=2
                j+=2
            return count + s[:idx[0]].count('*') + s[idx[-1]:].count('*')
        else:
            return s.count('*')
        
# Solution 2 (28 ms, 13.9 MB)

class Solution:
    def countAsterisks(self, s: str) -> int:
        cnt = 0
        idxs = [idx for idx, val in enumerate(s) if val == '|']
        for i in range(1, len(idxs) - 2, 2):
            arr = s[idxs[i] + 1:idxs[i+1]]
            cnt+=arr.count('*') 
        if idxs:
            cnt+=s[:idxs[0]].count('*')
            cnt+=s[idxs[-1]:].count('*')     
            return cnt
        else:  
            return s.count('*')

        