# Solution 1 (95 ms, 17.8 MB)

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        arr1 = []
        arr2 = []
        for i, val in enumerate(wordsDict):
            if word1 == val:
                arr1.append(i)
            elif word2 == val:
                arr2.append(i)
        arr3 = []
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                val = abs(arr1[i] - arr2[j])
                arr3.append(val)
        
        return min(arr3)

# Solution 2 (71 ms, 17.8 MB) (Best)

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        out = first = second = float('inf')
        for i, word in enumerate(wordsDict):
            if word == word1: 
                first = i
            elif word == word2: 
                second = i
            out = min(abs(first - second), out)
        return out