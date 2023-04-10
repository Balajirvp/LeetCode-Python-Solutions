# Solution 1 (30 ms, 13.9 MB)

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        arr = dict()
        for i in s:
            if i in arr:
                arr[i]+=1
                if arr[i] == 2:
                    return i
            else:
                arr[i]=1