# Solution 1 (192 ms, 33.4 MB)

import numpy as np

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return np.transpose(np.array(matrix))

# Solution 2 (83 ms, 17.1 MB)

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(zip(*matrix))

# Solution 3 (74 ms, 17.4 MB)

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        dict1 = defaultdict(list)
        for i1, v1 in enumerate(matrix):
            for i2, v2 in enumerate(v1):
                dict1[i2].append(v2)
        return dict1.values()