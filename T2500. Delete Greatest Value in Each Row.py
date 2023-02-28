# Solution 1 (124 ms, 13.9 MB)

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        cnt = 0
        val = []
        while(len(grid[0]) > 0):
            for i in range(len(grid)):
                idx = grid[i].index(max(grid[i]))
                val.append(grid[i].pop(idx))
            if i == len(grid) - 1:
                cnt+=max(val)
                val = []
        return cnt

# Solution 1 (93 ms, 14 MB) 

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        arr = [sorted(i, reverse = True) for i in grid]
        arr2 = list(zip(*arr))
        return sum(max(i) for i in arr2)