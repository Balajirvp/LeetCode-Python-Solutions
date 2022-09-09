# Solution 1 (271 ms, 16.6 MB)

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        odd = [i for i in nums if i % 2 != 0]
        even = [i for i in nums if i % 2 == 0]
        arr = [0]*n
        arr[0:n:2] = even[:]
        arr[1:n:2] = odd[:]
        return arr

# Solution 2 (236 ms, 16.2 MB) [LeetCode approach in case base array needs to be updated directly]

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        j = 1
        for i in range(0, len(nums), 2):
            if nums[i] % 2:
                while nums[j] % 2:
                    j += 2
                nums[i], nums[j] = nums[j], nums[i]
        return nums