# Solution 1 (171 ms, 14.2 MB)

from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        a = dict(Counter(nums))
        b = [(k,v) for k,v in a.items() if v % 2 == 0]
        c = [(k,v) for k,v in a.items()]
        return b == c

# Solution 1 (143 ms, 14.1 MB)

from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        a = dict(Counter(nums))
        b = {k:v for k,v in a.items() if v % 2 == 0}
        return a == b