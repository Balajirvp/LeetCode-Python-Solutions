# Solution 1 (110 ms, 14.5 MB)

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(0,len(nums),2):
            freq, val = nums[i], nums[i+1]
            for j in range(freq):
                arr.append(val)
        return arr

# Solution 2 (72 ms, 14.3 MB)

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(0,len(nums),2):
            freq, val = nums[i], nums[i+1]
            [arr.append(val) for j in range(freq)]
        return arr

