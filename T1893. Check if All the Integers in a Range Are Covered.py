# Solution 1 (52 ms, 14 MB)

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        rrange = [i for i in range(left, right+1, 1)]
        lrange = []
        for i in range(len(ranges)):
            lrange.extend([i for i in range(ranges[i][0], ranges[i][1] + 1, 1)])
        len1 = len(rrange)
        len2 = len(set(lrange) & set(rrange))
        return len1 == len2