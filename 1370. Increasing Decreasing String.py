# Solution 1 (69 ms, 13.8 MB)

class Solution:
    def sortString(self, s: str) -> str:
        arr = []
        ss = Counter(sorted(s))
        while sum(ss.values()) > 0:
            for idx in [idx for idx, val in ss.items() if val > 0]:
                arr.append(idx)
                ss[idx]-=1
            if sum(ss.values()) > 0:
                for idx in [idx for idx, val in ss.items() if val > 0][::-1]:
                    arr.append(idx)
                    ss[idx]-=1
        return ''.join(arr)
