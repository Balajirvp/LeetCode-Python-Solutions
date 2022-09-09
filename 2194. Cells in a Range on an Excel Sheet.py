# Solution 1 (58 ms, 13.8 MB)

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        str_start = ord(s[0])
        str_end = ord(s[3])
        num_start = int(s[1])
        num_end = int(s[4])
        arr = []
        for i in range(str_start, str_end + 1):
            for j in range(num_start, num_end + 1):
                arr.append(chr(i)+str(j))
        return arr
        