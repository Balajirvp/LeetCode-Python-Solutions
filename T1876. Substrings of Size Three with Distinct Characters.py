# Solution 1 (46 ms, 13.8 MB)

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        arr = [s[i:i+3] for i in range(len(s)) if len(s[i:i+3]) == 3]
        arr1 = [len(set(i)) for i in arr]
        arr2 = list(zip(arr,arr1))
        return sum(1 for i in range(len(arr2)) if arr2[i][1] == 3)