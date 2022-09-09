# Solution 1 (50 ms, 13.8 MB)

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        a = list(title.split())
        arr = []
        for i in a:
            if len(i) <= 2:
                arr.append(i.lower())
            else:
                arr.append(i.title())
        return ' '.join(arr)