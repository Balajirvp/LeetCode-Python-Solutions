# Solution 1: (9249 ms, 14.9 MB)

from itertools import combinations

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comb = combinations(nums,2)
        for num in comb:
            if sum(num) == target:
                final_num = num
                break
        a = nums.index(final_num[0])
        b = max(loc for loc, val in enumerate(nums) if val == final_num[1])
        return [a,b]

# Solution 2: (3841 ms, 14.9 MB)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

# Solution 3: (69 ms, 15.2 MB) (Using HashMap)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for idx, val in enumerate(nums):
            if target - val in dict1:
                return [dict1[target - val], idx]
            dict1[val] = idx