# Solution 1 (55 ms, 13.9 MB)

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums1)):
            val = nums2.index(nums1[i])
            arr.append(val)
        return arr

# Solution 1 (43 ms, 13.9 MB)

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [nums2.index(nums1[i]) for i in range(len(nums1))]
    