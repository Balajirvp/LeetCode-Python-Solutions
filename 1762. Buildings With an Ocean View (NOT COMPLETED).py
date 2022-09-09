

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        l = len(heights)
        ans = []
        for i in range(l):
            while ans and heights[ans[-1]] <= heights[i]:
                ans.pop()
            ans.append(i)
        return ans
