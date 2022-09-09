# Solution 1 (81 ms, 14 MB)

from collections import Counter

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums4 = dict(Counter(list(set(nums1)) + list(set(nums2)) + list(set(nums3))))
        return [k for k, v in nums4.items() if v >= 2]
        