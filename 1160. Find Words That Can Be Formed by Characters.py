# Solution 1 (193 ms, 14.6 MB)

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars1 = Counter(chars)
        count = 0
        l = len(words)
        for i in range(l):
            if Counter(words[i]) <= chars1:
                count+=len(words[i])
        return count    