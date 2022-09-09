# Solution 1 (314 ms, 32.7 MB)

import numpy as np

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return np.transpose(np.array(matrix))

# Solution 2 (138 ms, 14.7 MB)

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(zip(*matrix))