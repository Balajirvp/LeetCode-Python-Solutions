# Solution 1 (26 ms, 13.8 MB)

class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 != 0:
            return 'a'*n
        else:
            return 'a'*(n-1) + 'b'

# Solution 2 (31 ms, 13.8 MB)
      
class Solution:
    def generateTheString(self, n: int) -> str:
        val = ['a']*n
        if n % 2:
            return ''.join(val)
        else:
            val[-1] = 'b'
            return ''.join(val)

