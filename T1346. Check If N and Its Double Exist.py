# Solution 1 (81 ms, 14 MB)

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0) > 1:
            return True
        else:
            arr1 = [i/2 for i in arr if i != 0]
            return set(arr) & set(arr1)