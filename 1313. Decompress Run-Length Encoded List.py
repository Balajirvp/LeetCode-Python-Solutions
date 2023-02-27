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
    
# Solution 3 (71 ms, 14 MB)

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        idx = nums[::2]
        val = nums[1::2]
        comb = list(zip(idx, val))
        arr = []
        for i in comb:
            arr.append(i[0]*[i[1]])
        return [j for i in arr for j in i]

