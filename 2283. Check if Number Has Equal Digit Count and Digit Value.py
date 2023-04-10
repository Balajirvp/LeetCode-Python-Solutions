# Solution 1 (27 ms, 13.8 MB)

class Solution:
    def digitCount(self, num: str) -> bool:
        arr = defaultdict(int)
        arr.update(Counter(num))
        for i,v in enumerate(num):
            if int(v) == arr[str(i)]:
                continue
            else:
                return False
        return True
\
# Solution 2 (31 ms, 13.7 MB)

class Solution:
    def digitCount(self, num: str) -> bool:
        arr = Counter(num)
        for idx, val in enumerate(num):
            if int(val) == arr.get(str(idx), 0):
               continue
            else:
                return False
        return True