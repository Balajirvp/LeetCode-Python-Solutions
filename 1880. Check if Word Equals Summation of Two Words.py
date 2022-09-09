# Solution 1 (38 ms, 14 MB)

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        a = [chr(i) for i in range(97,107)]
        b = [i for i in range(10)]
        arr = dict(zip(a,b))
        val1 = ''.join([str(arr[i]) for i in firstWord])
        val2 = ''.join([str(arr[i]) for i in secondWord])
        val3 = ''.join([str(arr[i]) for i in targetWord])
        return int(val1) + int(val2) == int(val3)