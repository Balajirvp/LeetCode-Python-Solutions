# Solution 1 (119 ms, 15.2 MB)

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score1 = sorted(score, reverse = True)
        hashMap = {}
        for i in range(len(score1)):
            if i == 0:
                hashMap[score1[i]] = 'Gold Medal'
            elif i == 1:
                hashMap[score1[i]] = 'Silver Medal'
            elif i == 2:
                hashMap[score1[i]] = 'Bronze Medal'
            else:
                hashMap[score1[i]] =  str(i + 1)
        arr = []
        for i in score:
            arr.append(hashMap[i])
        return arr