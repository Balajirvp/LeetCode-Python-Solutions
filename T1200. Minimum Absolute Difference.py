# Memory Limit Exceeded (33/37 cases passed)

from itertools import combinations

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        a = combinations(arr,2)
        b = {tuple(i):abs(i[0] - i[1]) for i in a}
        minn = min(b.values())
        return [k for k,v in b.items() if v == minn]

# Solution 1 (481 ms, 28.6 MB)

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minn , res = inf, []
        for a,b in pairwise(arr):
            diff = b - a
            
            if diff < minn:
                res.clear()
                minn = diff
            
            if diff == minn:
                res.append([a,b])
        
        return res
            