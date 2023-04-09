# Solution 1 (31 ms, 13.9 MB)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        if l1 == l2:
            return ''.join(word1[i]+word2[i] for i in range(l1))
        elif l1 > l2:
            arr = ''.join(word1[i]+word2[i] for i in range(l2))
            return arr + word1[l2:]
        else:
            arr = ''.join(word1[i]+word2[i] for i in range(l1))
            return arr + word2[l1:]

# Solution 2 (31 ms, 14 MB)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        
        i = 0
        j = 0
        arr = ''
        
        while i < l1 and j < l2:
            arr+= word1[i] + word2[j]
            
            i+=1
            j+=1
            
        while i < l1:
            arr+= word1[i]
            i+=1
            
        while j < l2:
            arr+= word2[j]
            j+=1 
            
        return arr
    
# Solution 3 (24 ms, 13.9 MB)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = min(len(word1), len(word2))
        w1, w2 = word1, word2
        arr = []
        for i in range(l):
            arr.append(word1[i])
            arr.append(word2[i])
            w1 = w1.replace(word1[i], '', 1)
            w2 = w2.replace(word2[i], '', 1)
        arr.append(w1)
        arr.append(w2)
        return ''.join(arr)