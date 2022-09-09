# Solution 1 (637 ms, 26.9 MB)

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = [i for i in range(1, len(nums) + 1)]
        return set(n) - set(nums)

# Solution 2 (563 ms, 23.7 MB)

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