# Solution 1 (50 ms, 13.7 MB)

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i = 0
        while 4 ** i <= n:
            if 4 ** i == n:
                return True
            i+=1
        return False
                