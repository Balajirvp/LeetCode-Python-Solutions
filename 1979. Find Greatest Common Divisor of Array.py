# Solution 1 (73 ms, 14 MB)

from math import gcd

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        return gcd(nums[0], nums[-1])
        
# Solution 2 (73 ms, 14.1 MB)

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(nums[0],0,-1):
            if nums[-1] % i == 0 and nums[0] % i == 0:
                return i
                
# Solution 3 (73 ms, 13.9 MB)
# Euclidian way

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[0]
        b = nums[-1]
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a
                