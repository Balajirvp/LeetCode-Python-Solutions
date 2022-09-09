# Solution 1 (63 ms, 14.2 MB)

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        arr = Counter(moves)
        m = set(moves)
        ud = 1 if arr['U'] == arr['D'] else 0
        lr = 1 if arr['L'] == arr['R'] else 0
        if len(m) == 4:
            return ud + lr == 2
        elif len(m) == 2 and (('U' in m and 'D' in m) or ('R' in m and 'L' in m)):
            return ud == 1 or lr == 1
        else:
            return False