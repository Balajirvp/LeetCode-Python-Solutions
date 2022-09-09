# Solution 1 (70 ms, 13.9 MB)

class Solution:
    def maximum69Number (self, num: int) -> int:
        numm = [i for i in str(num)]
        for i in range(len(numm)):
            if numm[i] == '6':
                numm[i] = '9'
                break
        return int(''.join(numm))

# Solution 2 (38 ms, 13.9 MB)

class Solution:
    def maximum69Number (self, num: int) -> int:
        numm = [i for i in str(num)]
        try:
            idx = numm.index('6', 0)
        except:
            idx = -1
        if idx >= 0:
            numm[idx] = '9'
        return int(''.join(numm))
        