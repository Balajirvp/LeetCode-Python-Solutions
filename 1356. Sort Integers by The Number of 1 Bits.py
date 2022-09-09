# Solution 1 (95 ms, 14.1 MB)

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        dict1 = {i:bin(i).count('1') for i in arr}
        return sorted(arr, key = lambda x: dict1[x])

