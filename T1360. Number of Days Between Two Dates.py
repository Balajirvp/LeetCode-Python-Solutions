# Solution 1 (35 ms, 13.9 MB)

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        return abs((date.fromisoformat(date2) - date.fromisoformat(date1)).days)
        