# Solution 1 (34 ms, 13.9 MB)

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        word = list(word)
        for i in range(len(word)):
            if word[i] in 'abcdefghijklmnopqrstuvwxyz':
                word[i] = ' '
        arr = ''.join(word)
        res = arr.split()
        res = [int(i) for i in res]
        return len(set(res))