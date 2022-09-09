# Solution 1 (241 ms, 15.6 MB)

from statistics import Mode

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       return Mode(nums)


# Solution 2 (173 ms, 15.6 MB)

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       return Counter(nums).most_common(1)[0][0]

# Solution 3 (207 ms, 15.6 MB)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       return max(set(nums), key = nums.count)