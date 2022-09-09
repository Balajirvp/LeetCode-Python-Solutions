# Solution 1 (117 ms, 13.9 MB)

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dict1 = dict(paths)
        for i in dict1.values():
            if i not in dict1.keys():
                return i

# Solution 2 (57 ms, 14 MB)
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        a = set([paths[i][0] for i in range(len(paths))])
        b = set([paths[i][1] for i in range(len(paths))])
        return list(b - a)[0]