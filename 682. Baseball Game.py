# Solution 1 (41 ms, 13.9 MB)

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        for i in operations:
            if i.isdigit():
                arr.append(int(i))
            elif i[1:].isdigit():
                arr.append(int(i))
            elif i == '+':
                arr.append(arr[-1] + arr[-2])
            elif i == 'D':
                arr.append(arr[-1]*2)
            elif i == 'C':
                arr.pop()
        return sum(arr)