# Solution 1 (74 ms, 13.8 MB)

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = [''] * len(s)
        for i in range(len(s)):
            arr[indices[i]] = s[i]
        return ''.join(arr)

# Solution 2 (57 ms, 13.8 MB)  

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = ['NA']*len(indices)
        comb = list(zip(indices, list(s)))
        for i in comb:
            arr[i[0]] = i[1]
        return ''.join(arr)