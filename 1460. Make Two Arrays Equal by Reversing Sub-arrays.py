# Solution 1 (78 ms, 14.1 MB)

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)

# Solution 2 (81 ms, 14.1 MB)

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        arr1 = Counter(target)
        arr2 = Counter(arr)
        for idx, val in arr1.items():
            if val == arr2[idx]:
                continue
            else:
                return False
        return True