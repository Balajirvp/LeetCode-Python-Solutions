# Solution 1 (59 ms, 14 MB)

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i, val in enumerate(operations):
            if val =='++X' or val =='X++':
                x+=1
            elif val == '--X' or val == 'X--':
                x-=1
        return x

# Solution 2 (56 ms, 13.8 MB)

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        value = 0     
        dict1 = {"X++":1, "++X":1, "--X":-1, "X--":-1}
        for i in operations:
            value += dict1[i]     
        return value