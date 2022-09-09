# Solution 1 (108 ms, 14.5 MB)

from collections import Counter

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dict1 = Counter(words1)
        dict2 = Counter(words2)
        a = [k for k, v in dict1.items() if v == 1]
        b = [k for k, v in dict2.items() if v == 1]
        return sum(1 for i in a if i in b)

# Solution 2 (67 ms, 14.5 MB)

from collections import Counter

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dict1 = Counter(words1)
        dict2 = Counter(words2)
        count = 0
        for i in dict1.keys():
            if dict1[i] == 1 and dict2[i] == 1:
                count+=1
        return count
        