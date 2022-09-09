# Solution 1 (46 ms, 13.9 MB)

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        arr1 = Counter(word1)
        arr2 = Counter(word2)
        val = []
        for i,v in arr1.items():
            if i in arr2:
                val.append(abs(v - arr2[i]))
            else:
                val.append(v)
        for i,v in arr2.items():
            if i in arr1:
                val.append(abs(v - arr1[i]))
            else:
                val.append(v)
        if max(val) <= 3:
            return True
        else:
            return False