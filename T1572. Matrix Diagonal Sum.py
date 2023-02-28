# Solution 1 (112 ms, 14.1 MB)

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        mid = n//2
        total = sum([mat[i][i] + mat[i][n-1-i] for i in range(n)])
        if n % 2 != 0:
            total = total - mat[mid][mid]
        return total

# Solution 2 (374 ms, 32.4 MB)

import numpy as np
    
class Solution(object):
    def diagonalSum(self, mat):
        n = len(mat)
        summ = sum(np.diag(mat)) + sum(np.fliplr(mat).diagonal()) 
        if n % 2 == 1:
            summ = summ - mat[n//2][n//2] 
        return summ
    
# Solution 3 (113 ms, 14.1 MB)

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ = 0
        l = len(mat)
        for i in range(l):
            summ+= mat[i][i]
            summ+= mat[i][-1-i]
        if l % 2:
            summ-= mat[l//2][l//2]
        return summ
            