# Solution 1 (65 ms, 14.1 MB)

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        words1 = [Counter(i) for i in words]
        for i in range(len(words1) - 1):
            words1[i+1] = words1[i] & words1[i+1]   
        arr = []
        for k,v in words1[-1].items():
            for i in range(v):
                arr.append(k)
        return arr
        



