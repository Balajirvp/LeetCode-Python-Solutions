# Solution 1 (2080 ms, 38 MB)

import numpy as np

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        a = np.array(sorted(nums1))
        b = np.array(sorted(nums2, reverse = True))
        return a @ b
        
# Solution 2 (1128 ms, 23.2 MB)

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        a = sorted(nums1)
        b = sorted(nums2, reverse = True)
        return sum([a[i]*b[i] for i in range(len(a))])
        

# Actual solution based on question (1227, 19.2 MB)

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        counter_1 = [ 0 ] * 101  
        counter_2 = [ 0 ] * 101
        for i in nums1:
          counter_1[ i ] += 1
        for i in nums2:
          counter_2[ i ] += 1

        min_sum = 0
        i = 0
        j = 100
        while i <= 100 and j >= 0:
          if counter_1[ i ] == 0:
            i += 1
            continue
          if counter_2[ j ] == 0:
            j -= 1
            continue

          counter_1[ i ] -= 1
          counter_2[ j ] -= 1
          min_sum += i * j

        return min_sum
        
