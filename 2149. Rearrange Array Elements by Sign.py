# Solution 1 (2361 ms, 45.3 MB)

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [i for i in nums if i > 0]
        neg = [i for i in nums if i < 0]
        l = len(nums)
        arr = [0]*l
        j = 0
        k = 0
        for i in range(l):
            if i % 2 == 0:
                arr[i] = pos[j]
                j+=1
            else:
                arr[i] = neg[k]
                k+=1
        return arr