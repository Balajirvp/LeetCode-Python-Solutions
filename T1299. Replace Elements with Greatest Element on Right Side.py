# Solution 1 (6623 ms, 15.3 MB)

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            arr[i] = max(arr[(i+1):])
        arr[-1] = -1
        return arr

# Solution 2 (6056 ms, 15.5 MB)

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr = [max(arr[(i+1):]) for i in range(len(arr)-1)]
        arr = arr + [-1]
        return arr

# Solution 3 (788 ms, 15.9 MB)

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr1 = []
        maxx = -1
        for i in arr[::-1]:
            arr1.append(maxx)
            maxx = max(maxx, i)
        return arr1[::-1]
    
# Solution 4 (723 ms, 16.1 MB)

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        out = [-1]
        greatest = 0
        for num in arr[::-1]:
            if num > greatest:
                greatest = num
            out.append(greatest)
        out.pop()
        return out[::-1]