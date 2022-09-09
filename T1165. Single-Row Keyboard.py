# Solution 1 (88 ms, 13.9 MB)

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        b = list(word)
        move = keyboard.index(b[0])
        for i in range(1, len(b)):
            if i == 1:
                move+= abs(keyboard.index(b[i]) - move)
            else:
                move+= abs(keyboard.index(b[i]) - keyboard.index(b[i-1]))
        return move

# Solution 2 (61 ms, 14 MB)

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        a = {val:idx for idx, val in enumerate(keyboard)}
        move = prev_idx = 0
        for i in word:
            idx = a[i]
            move+= abs(idx - prev_idx)
            prev_idx = idx
        return move