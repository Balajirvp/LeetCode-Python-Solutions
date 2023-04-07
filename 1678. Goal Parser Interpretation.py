# Solution 1 (33 ms, 13.8 MB)

class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()', 'o').replace('(al)', 'al')
    
# Solution 2 (32 ms, 13.8 MB)

class Solution:
    def interpret(self, command: str) -> str:
        dict1 = {'G':'G', '()':'o', '(al)':'al'}
        arr = ''
        res = []
        for i in command:
            arr+=i
            if arr in dict1:
                res.append(dict1[arr])
                arr = ''
        return ''.join(res)
            