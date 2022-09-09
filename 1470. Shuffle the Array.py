# Solution 1 (108 ms, 14.1 MB)

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1, nums2 = nums[:n], nums[n:]
        nums3 = []
        for i in range(n):
            nums3.append(nums1[i])
            nums3.append(nums2[i])
        return nums3