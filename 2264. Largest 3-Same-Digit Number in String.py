# Solution 1 (48 ms, 13.8 MB)

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        arr = [num[i:i+3] for i in range(len(num)) if len(num[i:i+3]) == 3 and len(set(num[i:i+3])) == 1]
        if arr:
            return max(arr)
        else:
            return ''   