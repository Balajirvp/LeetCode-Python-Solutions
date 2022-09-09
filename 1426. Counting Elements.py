# Solution 1 (249 ms, 32 MB)

import numpy as np

class Solution:
    def countElements(self, arr: List[int]) -> int:
        a = np.array(arr)
        b = np.repeat(1, len(a))
        c = a + b
        return np.sum(1 for i in c if i in a)

# Solution 2 (58 ms, 14 MB)

class Solution:
    def countElements(self, arr: List[int]) -> int:
        a = [i + 1 for i in arr]
        return sum(1 for i in a if i in arr)
        
        