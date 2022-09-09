# Solution 1 (59 ms, 13.9 MB)

class Solution:
    def modifyString(self, s: str) -> str:
        l = len(s)
        arr = list(s)
        org = set(s)
        alpha = set([chr(i) for i in range(97,123)])
        diff = list(alpha - org)
        j = 1
        k = 3
        for i in range(l):
            if i == 0 and arr[i] == '?':
                arr[i] = diff[0]
            elif i == l - 1 and arr[i-1] == '?':
                arr[i] = diff[-1]
            elif arr[i] == '?':
                if i % 2 == 0:
                    arr[i] = diff[j]
                else:
                    arr[i] = diff[k]
        return ''.join(arr)