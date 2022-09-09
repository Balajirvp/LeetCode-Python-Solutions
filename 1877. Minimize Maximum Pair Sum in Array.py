# Solution 1 (2096 ms, 28 MB)

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        arr = [(nums[i], nums[-1-i]) for i in range(int(len(nums)/2))]
        return max(sum(i) for i in arr)
        
# Solution 2 (1230 ms, 28.6 MB)

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        start = 0
        end = l - 1
        arr = []
        while start < end:
            arr.append(nums[start] + nums[end])
            start+=1
            end-=1
        return max(arr)