# Solution 1 (122 ms  15.6 MB)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_final = []
        for i in range(len(nums)):
            if nums[i] in nums_final:
                continue
            else:
                nums_final.append(nums[i])
        
        nums[:] = nums_final
        return len(nums_final)