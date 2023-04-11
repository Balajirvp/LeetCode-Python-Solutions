# Solution 1 (59 ms, 14.2 MB)

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
        
# Solution 2 (59 ms, 13.9 MB)

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        arr = words[0]
        for i in words[1:]:
            arr = (Counter(i) & Counter(arr))
        arr2 = [[idx]*val for idx, val in arr.items()]
        return [j for i in arr2 for j in i]

