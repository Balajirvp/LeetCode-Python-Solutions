# Solution 1 (1032 ms, 14.3 MB)

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a = set([i for i in nums1 if i not in nums2])
        b = set([i for i in nums2 if i not in nums1])
        return [a,b]

# Solution 2 (177 ms, 14.3 MB)

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a = set(nums1) - set(nums2)
        b = set(nums2) - set(nums1)
        return [a,b]
