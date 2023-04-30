# Solution 1 (45 ms, 16.4 MB)

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
    

# Solution 2 (42 ms, 16.3 MB)

class Solution:
    def thousandSeparator(self, n: int) -> str:
        l = len(str(n))
        arr = str(n)[::-1]
        val = [arr[i:i+3] for i in range(0, l, 3)]
        return '.'.join(val)[::-1]
