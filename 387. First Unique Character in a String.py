# Solution 1 (61 ms, 14.2 MB)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        a = Counter(s)
        arr = [idx for idx, val in a.items() if val == 1]
        arr2 = [s.index(i) for i in arr]
        if arr2:
            return min(arr2)
        else:
            return -1