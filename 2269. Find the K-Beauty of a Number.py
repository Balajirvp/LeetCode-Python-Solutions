# Solution 1 (49 ms, 13.9 MB)

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num1 = str(num)
        l = len(num1)
        arr = [int(num1[i:j]) for i in range(l) for j in range(i + 1, l + 1) if len(num1[i:j]) == k and int(num1[i:j]) != 0]
        count = 0
        for i in arr:
            if num % i == 0:
                count+=1
        return count
        