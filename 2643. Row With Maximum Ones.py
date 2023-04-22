# Solution 1 (922 ms, 14.4 MB)

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        arr = {idx:val.count(1) for idx, val in enumerate(mat)}
        arr2 = sorted(arr.items(), key = lambda x: x[1], reverse = True)
        return arr2[0]