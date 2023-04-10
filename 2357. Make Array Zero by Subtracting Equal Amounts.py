# Solution 1 (41 ms, 13.9 MB)

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        while sum(nums) > 0:
            val = min([i for i in nums if i > 0])
            nums = [i - val for i in nums if i > 0]
            cnt+=1
        return cnt

# Solution 2 (23 ms, 13.9 MB)
    
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        arr = Counter(nums)
        if list(arr) == [0]:
            return 0
        else:
            return len([idx for idx, val in arr.items() if idx > 0])