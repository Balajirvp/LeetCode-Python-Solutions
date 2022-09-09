# Solution 1 (377 ms, 32.5 MB)

import numpy as np

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        matrix = np.array(matrix)
        m_min = np.min(matrix, axis = 1)
        m_max = np.max(matrix, axis = 0)
        return set(m_min) & set(m_max) 

# Solution 2 (377 ms, 32.5 MB)
# zip() can be used to transpose an iterable

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = [min(i) for i in matrix]
        n = [max(i) for i in list(zip(*matrix))]
        return set(m) & set(n)