# Solution 1 (41 ms, 14.1 MB)

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr1 = dict(Counter(arr))
        a = [v for k,v in arr1.items()]
        b = set(a)
        return len(a) == len(b)

# Solution 2 (35 ms, 13.9 MB)   

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        val = Counter(arr)
        cnt = Counter(val.values())
        return sum([1 for idx, val in cnt.items() if val > 1]) == 0