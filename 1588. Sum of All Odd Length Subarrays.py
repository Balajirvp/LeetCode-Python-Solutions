# Solution 1 (90 ms, 15 MB)

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        summ = 0
        res = [arr[i:i+j] for i in range(0,len(arr)) for j in range(1, len(arr)-i+1, 2)]
        for i in range(len(res)):
            summ+=sum(res[i])
        return summ
        
        