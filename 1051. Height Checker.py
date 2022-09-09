# Solution 1 (53 ms, 14 MB)

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights1 = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != heights1[i]:
                count+=1
        return count

# Solution 1 (39 ms, 13.8 MB)

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights1 = sorted(heights)
        return sum(heights[i] != heights1[i] for i in range(len(heights)))