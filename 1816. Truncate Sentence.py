# Solution 1 (23 ms, 13.8 MB)

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(i for i in s.split()[0:k])