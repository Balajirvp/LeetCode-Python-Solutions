# Solution 1 (40 ms, 13.9 MB)

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        arr = Counter(nums)
        a = sum([v for k, v in arr.items() if v == 1])
        b = sum([v for k, v in arr.items() if v % 2 == 0])
        c = sum([v//2 for k, v in arr.items() if (v > 1 and v % 2 == 1)])
        d = sum([v%2 for k, v in arr.items() if (v > 1 and v % 2 == 1)])
        return [int(b/2 + c), a + (b % 2) + d]
        
# Solution 2 (70 ms, 13.8 MB)

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        arr = Counter(nums)
        return [sum(i // 2 for i in arr.values()), sum(i % 2 for i in arr.values())]