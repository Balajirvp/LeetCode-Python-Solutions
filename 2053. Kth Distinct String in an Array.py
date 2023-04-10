# Solution 1 (391 ms, 14.1 MB)

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        arr = [i for i in arr if arr.count(i) == 1]
        if k > len(arr):
            return ''
        else:
            return arr[k-1]
    
# Solution 2 (74 ms, 14.1 MB)

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dict1 = {}
        for i in arr:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i] = 1
        arr1 = [k for k,v in dict1.items() if v == 1]
        if k > len(arr1):
            return ''
        else:
            return arr1[k-1]
        
# Solution 3 (74 ms, 14.1 MB)

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        val = Counter(arr)
        val2 = [i for i, v in val.items() if v == 1]
        if len(val2) >= k:
            return val2[k-1]
        else:
            return ''