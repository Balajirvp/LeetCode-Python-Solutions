# Solution 1 (33 ms, 13.8 MB)

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        arr1 = [i for i,v in Counter(s1.split()).items() if v == 1]
        arr2 = [i for i,v in Counter(s2.split()).items() if v == 1]
        a = set(arr2) - set(s1.split())
        b = set(arr1) - set(s2.split())
        return list(a | b)

# Solution 2 (32 ms, 13.9 MB)

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        a = s1.split() + s2.split()
        return [idx for idx, val in Counter(a).items() if val == 1]