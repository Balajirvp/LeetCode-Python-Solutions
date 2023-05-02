# Solution 1 (77 ms, 16.4 MB)

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        l = len(arr)
        idx = int((5*l)/100)
        new_arr = arr[idx : l - idx]
        return mean(new_arr)

# Solution 2 (83 ms, 16.4 MB)

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        l = len(arr)
        arr.sort()
        start = round(0.05*l)
        end = round(0.95*l)
        return mean(arr[start:end])