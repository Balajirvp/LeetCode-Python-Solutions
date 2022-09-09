# Solution 1 (50 ms, 13.8 MB)

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sent  = set(sentence)
        return len(sent) == 26