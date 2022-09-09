# Solution 1 (30 ms, 14 MB)

class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        for i in range(1, (n//2) + 1):
            arr.extend([i, -i])
        if n % 2 == 1:
            arr.append(0)
        return arr

# Solution 2 (36 ms, 13.9 MB)

class Solution:
    def sumZero(self, n: int) -> List[int]:
        return range(1-n, n, 2)
