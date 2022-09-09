# Solution 1 (37 ms, 13.8 MB)

class Solution:
    def interpret(self, command: str) -> str:
        a = command.replace('()','o')
        a = a.replace('(al)','al')
        return a