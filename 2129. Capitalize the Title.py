# Solution 1 (23 ms, 13.8 MB)

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        arr = []
        for i in title.split():
            if len(i) <= 2:
                arr.append(i.lower())
            else:
                arr.append(i.title())
        return ' '.join(arr)