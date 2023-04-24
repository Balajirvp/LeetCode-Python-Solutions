# Solution 1 (35 ms, 13.8 MB)

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        a = Counter(nums)
        b = [[k]*v for k,v in sorted(a.items(), key = lambda a: (a[1], -a[0]))]
        return [i for j in b for i in j]

# Solution 2 (59 ms, 13.9 MB)

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        arr = sorted(Counter(nums).items(), key = lambda x: (x[1], -x[0]))
        val = []
        for i in arr:
            temp = [i[0]]*i[1]
            val.extend(temp)
        return val