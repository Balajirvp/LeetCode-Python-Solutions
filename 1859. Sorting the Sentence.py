# Solution 1 (49 ms, 13.9 MB)

class Solution:
    def sortSentence(self, s: str) -> str:
        list1 = [[a[:-1],a[-1]] for a in list(s.split())]
        arr = sorted(list1, key = lambda a:a[1])
        arr1 = [a[0] for a in arr]
        return ' '.join(arr1)
    
# Solution 2 (27 ms, 13.8 MB)

class Solution:
    def sortSentence(self, s: str) -> str:      
        arr = ['NA']*len(s.split())
        for i in s.split():
            idx = int(i[-1])
            arr[idx-1] = i[:-1]
        return ' '.join(arr)