# Solution 1 (43 ms, 13.8 MB)

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        arr = []
        n1, n2 = int(s[1]), int(s[-1])
        start, end = ord(s[0]), ord(s[3])
        for i in range(start, end+1):
            for j in range(n1, n2+1):
                arr.append(chr(i)+str(j))
        return arr