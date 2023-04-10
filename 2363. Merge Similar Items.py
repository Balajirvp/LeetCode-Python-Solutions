# Solution 1 (128 ms, 14.8 MB)

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        ret = defaultdict(int)
        for i,v in dict(items1).items():
            ret[i]+=v
        for i,v in dict(items2).items():
            ret[i]+=v
        return sorted(ret.items())
        
# Solution 2 (118 ms, 14.6 MB)

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        a = dict(items1)
        b = dict(items2)
        arr = a.copy()
        for i in b:
            if i in arr:
                arr[i]+=b[i]
            else:
                arr[i]=b[i]
        return sorted(arr.items())