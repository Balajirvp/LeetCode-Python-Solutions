# Solution 1 (88 ms, 13.8 MB)

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        arr = []
        for i in range(left, right+1):
            if str(i).count('0'):
                continue
            else:
                a = [int(j) for j in str(i)]
                b = sum(1 for k in a if i % k != 0)
                if b == 0:
                    arr.append(i)
        return arr
        