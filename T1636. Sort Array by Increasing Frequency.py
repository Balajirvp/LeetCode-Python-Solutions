# Solution 1 (55 ms, 13.9 MB)

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        a = Counter(nums)
        b = [[k]*v for k,v in sorted(a.items(), key = lambda a: (a[1], -a[0]))]
        return [i for j in b for i in j]