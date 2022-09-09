# Solution 1 (45 ms  13.9 MB)

class Solution:
    def reverse(self, x: int) -> int:
        y = str(x)[::-1]
        if y[-1] == '-':
            if int(y[:-1]) >= -2**31 and int(y[:-1]) <= 2**31 - 1:
                return -1*int(y[:-1])
            else:
                return 0
        elif int(y) >= -2**31 and int(y) <= 2**31 - 1:
            return int(y)
        else:
            return 0
