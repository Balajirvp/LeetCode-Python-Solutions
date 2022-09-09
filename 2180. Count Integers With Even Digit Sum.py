# Solution 1 (106 ms, 13.8 MB)

class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(1, num + 1):
            a = list(str(i))
            b = sum([int(i) for i in a])
            if b % 2 == 0:
                count+=1
        return count

# Solution 2 (78 ms, 13.8 MB)

class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(1, num + 1):
            summ = 0
            for j in str(i):
                summ+=int(j)
            if summ % 2 == 0:
                count+=1
        return count