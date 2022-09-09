# Solution 1 (3171 ms, 36.3 MB)

import numpy as np

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = np.array(nums)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        return self.nums @ vec.nums
    
# Solution 2 (2377 ms, 18 MB)

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        return sum(self.nums[i]*vec.nums[i] for i in range(len(vec.nums)))
    