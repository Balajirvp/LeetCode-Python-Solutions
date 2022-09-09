# Solution 1 (166 ms, 14.8 MB)

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        ret = defaultdict(int)
        for i,v in dict(items1).items():
            ret[i]+=v
        for i,v in dict(items2).items():
            ret[i]+=v
        return sorted(ret.items(), key = lambda a: a[0])
        