# Solution 1 (58 ms, 14 MB)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 0
        while pow(2, i) <= n:
            if pow(2, i) == n:
                return True
            i+=1
        return False
            
# Solution 1 (51 ms, 13.8 MB)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        maxx = 2**30
        return n > 0 and maxx % n == 0
            