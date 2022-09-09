# Solution 1 (35 ms, 13.8 MB)

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        arr = []
        for i in range(0, n+1, 1):
            if i == 0:
                arr.append(0)
            elif i == 1:
                arr.append(1)
            elif i % 2 == 0:
                arr.append(arr[int(i/2)])
            elif i % 2 == 1:
                arr.append(arr[int((i + 1)/2)] + arr[int((i - 1)/2)])
        return max(arr)