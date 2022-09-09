# Solution 1 (49 ms, 13.9 MB)

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