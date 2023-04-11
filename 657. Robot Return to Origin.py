# Solution 1 (45 ms, 14.1 MB)

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        arr = Counter(moves)
        if arr['L'] == arr['R'] and arr['U'] == arr['D']:
            return True
        else:
            return False
