# Solution 1 (41 ms, 14.6 MB)

class Solution:
    def reverseWords(self, s: str) -> str:
        arr = list(s.split())
        for i in range(len(arr)):
            arr[i] = arr[i][::-1]
        return ' '.join(arr)
        