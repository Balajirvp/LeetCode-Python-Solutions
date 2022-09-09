# Solution 1 (37 ms, 13.9 MB)

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

# Solution 2 (43 ms, 14 MB)

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