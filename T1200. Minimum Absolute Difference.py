# Solution 1 (324 ms, 29 MB)

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

# Solution 2 (387 ms, 39.6 MB)

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        dict1 = {(arr[i], arr[i+1]): arr[i+1] - arr[i] for i in range(len(arr)-1)}
        v = min(dict1.values())
        return [list(idx) for idx, val in dict1.items() if val == v]