# Solution 1 (28 ms, 13.8 MB)

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        arr = [s[i:i+k] for i in range(0, len(s), k)]
        return [i if len(i) == k else i + fill*(k - len(i)) for i in arr]