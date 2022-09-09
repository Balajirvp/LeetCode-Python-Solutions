# Solution 1 (319 ms, 15 MB)

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        a = int(''.join(str(i) for i in num))
        b = a+k
        return [int(i) for i in str(b)]