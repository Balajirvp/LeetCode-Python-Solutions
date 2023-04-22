# Solution 1 (33 ms, 13.9 MB)

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        arr = zip(startTime, endTime)
        return sum(1 for i in arr if i[0] <= queryTime <= i[1])