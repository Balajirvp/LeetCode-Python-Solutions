# Solution 1 (711 ms, 15.3 MB)

class Solution:
    def largestOddNumber(self, num: str) -> str:
        summ = sum(1 for i in set(num) if int(i) % 2 != 0)
        l = len(num)
        if summ == 0:
            return ''
        else:
            for i in range(l):
                if int(num[:l-i]) % 2 == 1:
                    return num[:l-i]

# Solution 2 (62 ms, 15.1 MB)

class Solution:
    def largestOddNumber(self, num: str) -> str:
        l = len(num)
        for i in range(l-1, -1, -1):
            if int(num[i]) % 2: 
                return num[:i+1]  
        return ""
