# Solution 1 (195 ms, 33.5 MB)

from numpy import array

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        grid1 = array(grid)
        return len(grid1[grid1 < 0])

# Solution 2 (127 ms, 15.2 MB)

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        arr = [j for i in grid for j in i]
        return sum(1 for i in arr if i < 0)