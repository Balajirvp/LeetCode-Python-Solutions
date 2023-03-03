# Time limit exceeded (O(n2)) 200/210 cases passed

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subs = [sum(nums[i:i+j]) for i in range(len(nums)) for j in range(1, len(nums) - i + 1)]
        return max(subs)

# Dynamic Programming solution

# Solution 1 (772 ms  28.7 MB)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = maxx = nums[0]
        for num in nums[1:]:
            cur_max = max(num, cur_max + num)
            maxx = max(cur_max, maxx)
        return maxx
