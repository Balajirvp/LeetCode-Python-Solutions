# Solution 1 (27 ms, 13.8 MB)

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split()[:k])
    
