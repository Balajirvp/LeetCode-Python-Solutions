# Solution 1 (42 ms, 13.9 MB)

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        num1 = int(''.join([i for i in str(num)[::-1]]))
        num2 = int(''.join([i for i in str(num1)[::-1]]))
        return num == num2