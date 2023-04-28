# Solution 1 (57 ms, 16.4 MB)

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        a = [i % 2 for i in arr]
        count = 0
        for i in range(len(arr) - 2):
            if sum(a[i:i+3]) == 3:
                count+= 1
        return count

# Solution 2 (62 ms, 16.6 MB)

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        val = [i % 2 for i in arr]
        final = [sum(val[i:i+3]) for i in range(0, len(val))]
        if 3 in final:
            return True
        return False