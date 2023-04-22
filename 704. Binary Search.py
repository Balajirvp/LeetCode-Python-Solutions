# Solution 1 (242 ms, 15.4 MB)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        return -1
    
# Solution 2 (249 ms, 15.3 MB)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        arr = [idx for idx, val in enumerate(nums) if val == target]
        if arr:
            return arr[0]
        return -1