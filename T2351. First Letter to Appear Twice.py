# Solution 1 (30 ms, 13.9 MB)

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        a = list(s)                    
        b = defaultdict(int)
        for i in a:
            b[i] += 1
            if b[i] == 2:
                return i
                break

# Solution 2 (51 ms, 13.9 MB)

class Solution:
    def repeatedCharacter(self, s: str) -> str:                   
        b = defaultdict(int)
        for i in s:
            b[i] += 1
            if b[i] == 2:
                return i
                break
            
            
        