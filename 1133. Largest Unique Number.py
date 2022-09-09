# Solution 1 (100 ms, 14.1 MB)

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        a = Counter(nums)
        b = [k for k,v in a.items() if v == 1]
        if len(b) == 0:
            return -1
        else:
            return max(b)

# Solution 2 (68 ms, 14.1 MB)

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums.sort()
        a = Counter(nums)
        val = -1
        if len(nums) == 1:
            return max(nums)
        else:
            for i in range(len(nums) - 1, -1, -1):
                if a[nums[i]] == 1:
                    val = nums[i]
                    break
                else:
                    continue
            return val
        