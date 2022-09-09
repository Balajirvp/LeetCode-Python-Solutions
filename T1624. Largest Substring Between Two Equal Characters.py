# Solution 1 (72 ms, 13.7 MB)

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        arr = Counter(s)
        arr1 = [i for i, v in arr.items() if v > 1]
        dict1 = {}
        for i in arr1:
            a = [j for j,v in enumerate(s) if v == i]
            dict1[i] = a
        arr2 = []
        for i in dict1:
            val = max(dict1[i]) - min(dict1[i]) - 1
            arr2.append(val)
        if arr2:
            return max(arr2)
        else:
            return -1

# Solution 2 (55 ms, 13.8 MB)    

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        arr = Counter(s)
        arr1 = [i for i, v in arr.items() if v > 1]
        dict1 = {}
        for i in arr1:
            a = [j for j,v in enumerate(s) if v == i]
            dict1[i] = a
        arr2 = []
        for i, v in dict1.items():
            val = max(v) - min(v) - 1
            arr2.append(val)
        if arr2:
            return max(arr2)
        else:
            return -1
        