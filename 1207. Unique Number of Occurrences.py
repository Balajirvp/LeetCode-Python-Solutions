# Solution 1 (46 ms, 14.1 MB)

from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr1 = dict(Counter(arr))
        a = [v for k,v in arr1.items()]
        b = set(a)
        return len(a) == len(b)