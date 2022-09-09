# Solution 1 (144 ms, 20.6 MB)

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        val = [i.upper() if i.isalpha() else i for i in s[::-1] if i not in '-']
        arr = []
        for i in range(0, len(val), k):
            arr.append(''.join(val[i:i+k]))
        arr1 = [i[::-1] for i in arr[::-1]]
        return '-'.join(arr1)