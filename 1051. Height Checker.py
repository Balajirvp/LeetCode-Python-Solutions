# Solution 1 (38 ms, 13.9 MB)

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights1 = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != heights1[i]:
                count+=1
        return count

# Solution 1 (39 ms, 13.7 MB)

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights1 = sorted(heights)
        return sum(heights[i] != heights1[i] for i in range(len(heights)))
    
# Solution 3 (36 ms, 13.9 MB)

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp = sorted(heights)
        arr = zip(heights, exp)
        val = sum([1 for i in arr if i[0] - i[1] != 0])
        return val