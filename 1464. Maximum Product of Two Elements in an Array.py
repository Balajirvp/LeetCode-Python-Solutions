# Solution 1 (83 ms, 13.9 MB)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] - 1)*(nums[-2]-1)

# Solution 2 (48 ms, 14 MB)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first, second = 0, 0      
        for number in nums:          
            if number > first:
                first, second = number, first               
            elif number > second:
                second = number
        return (first - 1) * (second - 1)