# Solution 1 (218 ms, 14.1 MB)

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        cnt = 0
        for i in arr1:
            if count == len(arr2):
                cnt+=1
            count = 0
            for j in arr2:
                if abs(i - j) <= d:
                    break
                count+=1   
        if count == len(arr2):
            cnt+=1
        return cnt

# Solution 2 (111 ms, 14.1 MB)       # Binary search solution

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        dist = len(arr1)
        for num in arr1:
            start = 0
            end = len(arr2) - 1
            while start <= end:
                mid = (start + end)//2
                if abs(num - arr2[mid]) <= d:
                    dist-= 1
                    break
                elif arr2[mid] - num > 0:
                    end = mid - 1
                elif arr2[mid] - num < 0:
                    start = mid + 1
        return dist
                