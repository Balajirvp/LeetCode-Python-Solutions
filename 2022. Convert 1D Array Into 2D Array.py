# Solution 1 (1654 ms, 20.5 MB)

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        arr = []
        if len(original) == m*n:
            for i in range(0, len(original), n):
                arr.append(original[i:i+n])
            return arr
        else:
            return []

# Solution 2 (1362 ms, 37.2 MB)

import numpy as np 

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) == m*n:
            return np.array(original).reshape(m,n)
        else:
            return []