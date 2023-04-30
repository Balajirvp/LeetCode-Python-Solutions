# Solution 1 (50 ms, 16.5 MB)

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = Counter(nums1) & Counter(nums2)
        val = [[i]*v for i,v in arr.items()]
        return [j for i in val for j in i]