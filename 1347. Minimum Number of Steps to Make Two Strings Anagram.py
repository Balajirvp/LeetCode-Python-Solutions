# Solution 1 (118 ms, 14.5 MB)

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        arr = Counter(t) - Counter(s)
        return sum([val for idx, val in arr.items()])