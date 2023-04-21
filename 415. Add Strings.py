# Solution 1 (34 ms, 13.8 MB)

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))

# Solution 2 (49 ms, 14 MB) - Solution according to the given question (without directly using int)

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:       
        def str2int(num):
            dict1 = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}
            cnt = 0
            for i in num:
                cnt = cnt * 10 + dict1[i]
            return cnt
        return str(str2int(num1) + str2int(num2)) 