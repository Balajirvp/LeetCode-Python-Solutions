# Solution 1 (34 ms, 13.8 MB)

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        word = sorted(words, key = len)
        arr = []
        for idx, val in enumerate(word):
            a = word[idx + 1:]
            cnt = sum([1 for i in a if val in i])
            if cnt > 0:
                arr.append(val)
        return arr