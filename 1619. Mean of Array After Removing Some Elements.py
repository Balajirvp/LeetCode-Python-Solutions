# Solution 1 (64 ms, 13.9 MB)

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        l = len(arr)
        idx = int((5*l)/100)
        new_arr = arr[idx : l - idx]
        return mean(new_arr)