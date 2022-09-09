# Solution 1 (827 ms, 14.6 MB)

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        arr = [0]*len(rectangles)
        count = 0
        for i in range(len(rectangles)):
            arr[i] = min(rectangles[i][:])
        for i in range(len(arr)):
            if arr[i] == max(arr):
                count+=1
        return count

# Solution 1 (228 ms, 14.5 MB)

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        arr = [0]*len(rectangles)
        count = 0
        for i in range(len(rectangles)):
            arr[i] = min(rectangles[i][:])
        return arr.count(max(arr))