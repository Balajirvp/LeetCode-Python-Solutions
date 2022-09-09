# Solution 1 (341 ms, 35.5 MB)

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr1 = sorted(set(arr))
        dict1 = {val:idx for idx, val in enumerate(arr1)}
        arr2 = [0]*len(arr)
        for i in range(len(arr)):
            arr2[i] = dict1[arr[i]] + 1
        return arr2
                