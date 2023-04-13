# Solution 1 (67 ms, 13.8 MB)

class Solution:
    def dayOfYear(self, date: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year, month, day = (int(i) for i in date.split('-'))
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days[1] = 29
        return day + sum(days[:month - 1])