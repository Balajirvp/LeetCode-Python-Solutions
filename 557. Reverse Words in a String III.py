# Solution 1 (41 ms, 14.6 MB)

class Solution:
    def reverseWords(self, s: str) -> str:
        arr = list(s.split())
        for i in range(len(arr)):
            arr[i] = arr[i][::-1]
        return ' '.join(arr)

# Solution 2 (30 ms, 14.6 MB)
     
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(list(map(lambda x: x[::-1], s.split())))