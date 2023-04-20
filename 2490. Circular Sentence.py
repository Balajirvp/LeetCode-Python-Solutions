# Solution 1 (29 ms, 13.8 MB)

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        idx1 = [i[0]  for i in sentence.split()]
        idx2 = [sentence.split()[-1][-1]] + [i[-1] for i in sentence.split()[:-1]]  
        return idx1 == idx2