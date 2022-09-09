# Solution 1 (354 ms, 32.7 MB)

import numpy as np

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        try: 
            return np.array(mat).reshape(r,c)
        except:
            return mat

# Solution 2 (134 ms, 14.8 MB)

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        arr = [i for j in mat for i in j]
        if r*c == len(arr):
            return [arr[i*c:(1+i)*c] for i in range(r)]
        else:
            return mat