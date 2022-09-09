# Solution 1 (672 ms, 15.5 MB)

from itertools import combinations

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        comb = list(combinations(nums,2))
        count = 0
        for i in range(len(comb)):
            if abs(comb[i][1] - comb[i][0]) == k:
                count+=1
        return count
        
# Solution 2 (239 ms, 13.8 MB)

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    count+=1
        return count
        
# Solution 3 (91 ms, 14 MB)

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        dict1 = {}
        for i in nums:
            if i in dict1:
                dict1[i] +=1
            else:
                dict1[i] = 1
        for i in dict1:
            if i+k in dict1:
                count+=dict1[i]*dict1[i+k]
                
        return count