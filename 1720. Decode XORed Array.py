# Solution 1 (240 ms, 15.8 MB)

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first,]
        for i in range(len(encoded)):
            val = arr[-1]^encoded[i]
            arr.append(val)
        return arr

