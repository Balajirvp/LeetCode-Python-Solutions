# Solution 1 (882 ms, 27.1 MB)

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        arr = []
        total = sum(shifts) % 26
        for i, v in enumerate(s):
            diff = ord(v) - ord('a')
            arr.append(ord('a') + (diff + total) % 26)
            total = (total - shifts[i]) % 26
        return ''.join([chr(i) for i in arr])
        