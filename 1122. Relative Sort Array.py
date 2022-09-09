# Solution 1 (54 ms, 14.2 MB)

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]: 
        a = set(arr1) - set(arr2)
        b = sorted([i for i in arr1 if i in a])
        ar1 = Counter(arr1)
        ar2 = []
        for i in arr2:
            ar2.append([i]*ar1[i])
        arr = [i for j in ar2 for i in j]
        return arr + b
    