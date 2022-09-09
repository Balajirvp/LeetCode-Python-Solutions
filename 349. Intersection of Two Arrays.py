# Solution 1 (54 ms, 14.1 MB)

from collections import Counter

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = list(set(nums1)) + list(set(nums2))
        b = dict(Counter(a))
        return [k for k,v in b.items() if v == 2]
        
# Solution 2 (60 ms, 14.1 MB)

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2)
        