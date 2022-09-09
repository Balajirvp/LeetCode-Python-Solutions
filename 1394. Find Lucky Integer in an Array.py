# Solution 1 (79 ms, 13.9 MB)

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        a = Counter(arr)
        b = [k for k,v in a.items() if k == v]
        if b:
            return max(b)
        else:
            return -1