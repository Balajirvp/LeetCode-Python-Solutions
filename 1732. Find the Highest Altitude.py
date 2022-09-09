# Solution 1 (37 ms, 13.8 MB)

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arr = [0]*(len(gain)+1)
        for i in range(len(gain)):
            arr[i+1] = arr[i] + gain[i]
        return max(arr)