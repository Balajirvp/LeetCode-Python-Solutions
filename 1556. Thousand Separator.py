# Solution 1 (37 ms, 13.9 MB)

class Solution:
    def thousandSeparator(self, n: int) -> str:
        arr = list(str(n))
        l = len(arr)
        for i in range(l, 0, -3):
            if i == l:
                continue
            else:
                arr.insert(i, '.')
        return ''.join(arr)