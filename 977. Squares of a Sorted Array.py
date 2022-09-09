# Solution 1 (404 ms, 16.2 MB)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = [i*i for i in nums]
        return sorted(arr)

# Solution 2 (264 ms, 16.3 MB)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = [i*i for i in nums]
        arr.sort()
        return arr

