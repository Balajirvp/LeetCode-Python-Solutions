# Solution 1 (45 ms, 13.9 MB)

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        arr = list(number)
        arr1 = list(number)
        idx = [i for i, v in enumerate(arr) if v == digit]
        res = []
        for i in idx:
            arr1.pop(i)
            res.append(''.join(arr1))
            arr1 = arr[:]
        return max(res)

# Solution 2 (28 ms, 13.9 MB)

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        idxs = [i for i, v in enumerate(number) if v == digit]
        arr = []
        for i in idxs:
            arr.append(number[:i] + number[i+1:])
        arr2 = [int(i) for i in arr]
        return str(max(arr2))