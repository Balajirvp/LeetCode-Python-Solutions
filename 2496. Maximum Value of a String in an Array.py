# Solution 1 (30 ms, 13.9 MB)

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        arr = []
        for i in strs:
            if i.isdigit():
                arr.append(int(i))
            else:
                arr.append(len(i))
        return max(arr)