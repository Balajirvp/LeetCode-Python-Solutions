# Solution 1 (653 ms, 14 MB)

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums1 = sorted(nums)
        final = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] > nums1[j]:
                    count+=1
            final.append(count)
        return final

# Solution 2 (476 ms, 14 MB)

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [sorted(nums).index(i) for i in nums]
            
# Solution 3 (259 ms, 14 MB)

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            res.append(sum([j < i for j in nums]))
        return res