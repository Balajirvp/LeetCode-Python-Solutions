# Solution 1 (25 ms, 13.8 MB)

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = n -1
        b = 1
        while '0' in set(str(a)) or '0' in set(str(b)):
            a-=1
            b+=1
        return [a,b]