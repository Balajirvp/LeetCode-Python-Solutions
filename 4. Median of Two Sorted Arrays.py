# Solution 1 (175 ms  14.1 MB)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) % 2 != 0:
            return nums1[ceil(len(nums1)/2) - 1]
        elif len(nums1) % 2 == 0:
            return (nums1[int((len(nums1)/2) - 1)] + nums1[int(len(nums1)/2)])/2

# Solution 2 (84 ms  14.1 MB)
        
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_list = sorted(nums1 + nums2)
        l = len(new_list)
        if l % 2:
            return new_list[l//2]
        else:
            return (new_list[int(l/2)] + new_list[int(l/2) - 1])/2
