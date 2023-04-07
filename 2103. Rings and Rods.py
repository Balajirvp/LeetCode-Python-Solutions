# Solution 1 (29 ms, 13.9 MB)

class Solution:
    def countPoints(self, rings: str) -> int:
        keys = [i for i in range(10)]
        rods = {k: [] for k in keys}
        cnt = 0
        ring = [rings[i:i+2] for i in range(0, len(rings), 2)]
        for i in ring:
            rods[int(i[1])].append(i[0])
        for i in rods.values():
            if len(set(i)) == 3:
                cnt+=1
        return cnt