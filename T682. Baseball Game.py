# Solution 1 (352 ms, 14.1 MB)

class Solution:
    def calPoints(self, ops: List[str]) -> int:
            i = 0
            while i < len(ops):
                if ops[i].lstrip('-').isdigit():
                    i+=1
                    continue
                elif ops[i] == 'C':
                    ops.remove(ops[i-1])
                    ops.remove(ops[i-1])
                    i = 0
                    continue
                elif ops[i] == 'D':
                    ops[i] = str(int(ops[i-1])*2)
                    i = 0
                    continue
                elif ops[i] == '+':
                    ops[i] = str(int(ops[i-1]) + int(ops[i-2]))
                    i = 0
                    continue
            return sum([int(i) for i in ops])

# Solution 2 (80 ms, 14 MB)

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        arr = []
        for i in range(len(ops)):
            match ops[i]:
                case '+':
                    arr.append(int(arr[-1]) + int(arr[-2]))
                case 'C':
                    arr.pop()
                case 'D':
                    arr.append(arr[-1]*2)
                case _:
                    arr.append(int(ops[i]))
        return sum(arr)

# Solution 3 (54 ms, 14.1 MB)

class Solution: 
    def calPoints(self, ops: List[str]) -> int:
        arr = []
        for i in range(len(ops)):
            if ops[i] == '+':
                arr.append(arr[-1] + arr[-2])
            elif ops[i] == 'C':
                arr.pop()
            elif ops[i] == 'D':
                arr.append(arr[-1]*2)
            else:
                arr.append(int(ops[i]))
        return sum(arr)