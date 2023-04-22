# Solution 1 (39 ms, 13.9 MB)

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arr = [0]*(len(gain)+1)
        for i in range(len(gain)):
            arr[i+1] = arr[i] + gain[i]
        return max(arr)

# Solution 2 (36 ms, 13.9 MB)

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arr = [sum(gain[:i]) for i in range(1, len(gain) + 1)]
        val = max(arr)
        if val > 0:
            return val
        else:
            return 0
