# Solution 1 (45 ms, 13.8 MB)

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        arr = []
        for i in range(len(index)):
            arr.insert(index[i], nums[i])
        return arr

# Solution 2 (46 ms, 13.8 MB)

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        arr = []
        [arr.insert(index[i], nums[i]) for i in range(len(index))]
        return arr
