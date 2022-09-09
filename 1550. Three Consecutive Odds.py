# Solution 1 (46 ms, 13.9 MB)

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        a = [i % 2 for i in arr]
        count = 0
        for i in range(len(arr) - 2):
            if sum(a[i:i+3]) == 3:
                count+= 1
        return count