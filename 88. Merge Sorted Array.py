# Solution 1 (63 ms, 13.8 MB)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:] = nums1[0:m]
        nums1.extend(nums2)
        nums1.sort()