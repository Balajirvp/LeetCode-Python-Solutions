# Solution 1 (310 ms, 32.4 MB)

import numpy as np

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        return np.intersect1d(np.intersect1d(np.array(arr1), np.array(arr2)), np.array(arr3))

# Solution 2 (87 ms, 14.4 MB)

from collections import Counter

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        arr = dict(Counter(arr1 + arr2 + arr3))
        return sorted([k for k, v in arr.items() if v == 3])

        