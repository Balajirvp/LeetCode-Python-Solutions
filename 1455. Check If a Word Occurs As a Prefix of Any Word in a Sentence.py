# Solution 1 (23 ms, 13.8 MB)

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l = len(searchWord)
        arr = [idx for idx, val in enumerate(sentence.split()) if val[:l] == searchWord]
        if arr:
            return min(arr) + 1
        else:
            return -1 
        
