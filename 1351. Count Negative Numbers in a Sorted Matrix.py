# Solution 1 (358 ms, 33.5 MB)

from numpy import array

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        grid1 = array(grid)
        return len(grid1[grid1 < 0])

# Solution 2 (358 ms, 33.5 MB)

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        grid1 = [grid[i][j] for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] < 0]
        return len(grid1)