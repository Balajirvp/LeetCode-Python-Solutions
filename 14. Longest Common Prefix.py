# Solution 1 (35 ms, 14 MB)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        arr = []
        l = min(len(i) for i in strs)
        for i in range(l):
            arr.append([j[i] for j in strs])
        val = [len(set(val)) for idx, val in enumerate(arr)]
        for i, v in enumerate(val):
            if v != 1:
                return strs[0][:i]
        return strs[0][:l]
        
