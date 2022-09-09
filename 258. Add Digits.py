# Solution 1 (52 ms, 13.9 MB)

class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            num = sum([int(i) for i in str(num)])
        return num
