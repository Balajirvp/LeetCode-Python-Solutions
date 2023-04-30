# Solution 1 (75 ms, 17.2 MB)

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        l = len(arr)
        i = 0
        while i < l:
            if arr[i] == 0:
                arr.insert(i+1, 0)
                arr.pop()
                i+=2
            else:
                i+=1

# Solution 2 (76 ms, 17.2 MB)

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l = len(arr)
        val = []
        for i, v in enumerate(arr):
            if v == 0:
                val.append(0)
                val.append(0)
            else:
                val.append(v)
        arr[:] = val[:l]