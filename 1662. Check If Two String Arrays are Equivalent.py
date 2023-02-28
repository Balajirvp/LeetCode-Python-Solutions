# Solution 1 (34 ms, 13.9 MB)

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)
    
# Solution 2 (33 ms, 13.9 MB)

class Solution:
    def generate(self, wordlist: List[str]):
        for word in wordlist:
            for char in word:
                yield char
        yield None

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        for c1, c2 in zip(self.generate(word1), self.generate(word2)):
            if c1 != c2:
                return False
        return True