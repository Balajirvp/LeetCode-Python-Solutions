# Solution 1 (1047 ms, 16.1 MB)

class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        for i in s:
            if len(stack) > 1 and stack[-1] == stack[-2] == i:
                stack.pop()
            stack.append(i)
        return ''.join(stack)