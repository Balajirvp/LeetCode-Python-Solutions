# Solution 1 (74 ms, 13.8 MB)

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = [''] * len(s)
        for i in range(len(s)):
            arr[indices[i]] = s[i]
        return ''.join(arr)
    