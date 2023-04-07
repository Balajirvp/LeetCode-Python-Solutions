# Solution 1 (30 ms, 13.8 MB) 

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        R, L = [], []
        cnt = 0
        for i in s:
            if i == 'R':
                R.append('R')
            else:
                L.append('L')
            if len(R) == len(L):
                cnt+=1
        return cnt