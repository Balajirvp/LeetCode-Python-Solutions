# Solution 1 (49 ms, 13.9 MB)

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alpha = [chr(i) for i in range(65, 91)]
        nums  = [i for i in range(1, 27)]
        comb = dict(zip(alpha,nums))
        summ = 0
        l = len(columnTitle)
        for i in range(l):
            summ+= pow(26, l - 1 - i)*comb[columnTitle[i]]
        return summ
            