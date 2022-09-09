# Solution 1 (192 ms, 16.3 MB)

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums1 = Counter(nums)
        num1 = [k for k, v in nums1.items() if v == 2]
        
        nums2, l = sum(set(nums)), len(nums)
        num2 = int( (l*(l+1)) / 2 ) - nums2
        num1.append(num2)
        return num1