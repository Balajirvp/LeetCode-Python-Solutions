# Solution 1 (201 ms, 16.2 MB)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([i*i for i in nums])

# Solution 2 (201 ms, 16.1 MB)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = [i*i for i in nums]
        arr.sort()
        return arr

