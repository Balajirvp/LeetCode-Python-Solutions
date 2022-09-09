# Solution 1 (45 ms, 13.8 MB)

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        arr1 = [i for i,v in Counter(s1.split()).items() if v == 1]
        arr2 = [i for i,v in Counter(s2.split()).items() if v == 1]
        a = set(arr2) - set(s1.split())
        b = set(arr1) - set(s2.split())
        return list(a | b)
        
        