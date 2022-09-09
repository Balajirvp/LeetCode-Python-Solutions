# Solution 1 (42 ms, 13.9 MB)

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        arr = [s[i:i+k] for i in range(0, len(s), k)]
        if len(arr[-1]) == k:
            return arr
        else:
            l = len(arr[-1])
            arr[-1] = arr[-1] + (k-l)*fill
            return arr