# Solution 1 (54 ms, 14 MB)

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        a = list(zip(startTime, endTime))
        count = 0
        for i in range(len(a)):
            if list(a[i])[0] <= queryTime and list(a[i])[-1] >= queryTime:
                count+=1
        return count