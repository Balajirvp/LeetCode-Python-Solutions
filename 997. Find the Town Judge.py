# Solution 1 (783 ms, 19.2 MB)

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        arr1 = []
        arr2 = []
        for i in range(len(trust)):
            arr1.append(trust[i][1])
            arr2.append(trust[i][0])
        arr = Counter(arr1)
        res = [i for i,v in arr.items() if v == n - 1 and i not in arr2]  
        if res:
            return res[0]
        elif n == 1:
            return 1
        else:
            return -1
        