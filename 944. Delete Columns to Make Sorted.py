# Solution 1 (166 ms, 16.1 MB)

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        arr = [list(i) for i in strs]
        arr1 = list(zip(*arr))
        count = 0
        l = len(arr1)
        for i in range(l):
            if sorted(arr1[i]) != list(arr1[i]):
                count+=1
        return count