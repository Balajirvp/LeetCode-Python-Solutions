# Solution 1 (48 ms, 13.8 MB)

class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()

# Solution 2 (34 ms, 13.8 MB)

class Solution:
    def toLowerCase(self, s: str) -> str:
        is_upper = lambda x : 'A' <= x <= 'Z'
        to_lower = lambda x : chr(ord(x) + 32)
        
        return ''.join([to_lower(x) if is_upper(x) else x for x in s])
    
# Solution 3 (24 ms, 13.8 MB)

class Solution:
    def toLowerCase(self, s: str) -> str:
        arr = [(chr(ord(i) + 32) if ord(i) >= 65 and ord(i) <= 90 else i) for i in s]
        return ''.join(arr)