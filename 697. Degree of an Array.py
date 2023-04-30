# Solution 1 (795 ms, 17.8 MB)

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        arr = Counter(nums)
        deg = max(arr.values())
        val = [i for i, v in arr.items() if v == deg]
        l = len(nums)
        ans = []
        for i in val:
            ans.append(l - nums[::-1].index(i) - nums.index(i))
        return min(ans)