# Solution 1 (44 ms, 14 MB)

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        val = 0
        for i in range(len(sentences)):
            val = max(len(sentences[i].split()), val)
        return val