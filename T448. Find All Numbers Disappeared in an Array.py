# Solution 1 (348 ms, 28.6 MB)
    
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = range(1, len(nums)+1)
        return set(arr) - set(nums)

# Solution 2 (344 ms, 26.8 MB)

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hash_table = {}
        for num in nums:
            hash_table[num] = 1
        result = []    
        for num in range(1, len(nums) + 1):
            if num not in hash_table:
                result.append(num)               
        return result          
    
