# Solution 1 (175 ms  14.1 MB)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) % 2 != 0:
            return nums1[ceil(len(nums1)/2) - 1]
        elif len(nums1) % 2 == 0:
            return (nums1[int((len(nums1)/2) - 1)] + nums1[int(len(nums1)/2)])/2