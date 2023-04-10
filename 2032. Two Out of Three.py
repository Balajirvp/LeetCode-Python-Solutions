# Solution 1 (72 ms, 13.8 MB)

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums4 = Counter(list(set(nums1)) + list(set(nums2)) + list(set(nums3)))
        return [k for k, v in nums4.items() if v >= 2]

# Solution 2 (70 ms, 13.7 MB)
      
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        a = set(nums1) & set(nums2)
        b = set(nums1) & set(nums3)
        c = set(nums2) & set(nums3)
        d = list(a) + list(b) + list(c)
        return set(d)