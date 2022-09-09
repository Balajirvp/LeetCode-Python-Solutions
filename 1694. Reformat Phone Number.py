# Solution 1 (56 ms, 13.9 MB)

class Solution:
    def reformatNumber(self, number: str) -> str:
        a = [i for i in number if i not in ('-',' ')]
        l = len(a)
        arr = []
        while l > 4:
            arr.append(''.join(a[:3]))
            a = a[3:]
            l-=3
        if len(a) <= 3:
            arr.append(''.join(a))
        else:
            arr.append(''.join(a[:2]))
            arr.append(''.join(a[2:]))
        return '-'.join(arr)