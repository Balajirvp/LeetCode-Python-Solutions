# Solution 1 (107 ms, 14.8 MB)

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums1 = [i for i in nums if i%2 == 0]
        nums2= [i for i in nums if i%2 != 0]
        return nums1 + nums2