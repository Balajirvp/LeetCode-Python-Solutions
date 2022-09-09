# Solution 1 (85 ms, 13.9 MB)

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        a = sorted([nums[i] for i in range(len(nums)) if i % 2 == 0])
        b = sorted([nums[i] for i in range(len(nums)) if i % 2 == 1], reverse = True)
        arr = []
        j = 0
        k = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                arr.append(a[j])
                j+=1
            elif i % 2 == 1:
                arr.append(b[k])
                k+=1
        return arr
            
        