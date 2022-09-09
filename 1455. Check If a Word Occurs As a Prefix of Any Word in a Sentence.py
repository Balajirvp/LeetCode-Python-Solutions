# Solution 1 (53 ms, 14 MB)

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l = len(searchWord)
        arr = [i for i in sentence.split() if len(i) >= l]
        res = []
        for i in arr:
            if searchWord == i[:l]:
                res.append(i)
        result = [idx+1 for idx, val in enumerate(sentence.split()) if val in res]
        if result:
            return min(result)
        else:
            return -1