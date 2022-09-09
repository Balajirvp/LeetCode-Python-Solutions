# Solution 1 (55 ms, 14 MB)

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        left,right= 0, 0
        count = 0
        for i in range(len(s)):
            if s[i]=='L':
                left+=1
            else:
                right+=1
            if left == right:
                count+=1
        return count