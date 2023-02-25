# Time limit exceeded

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arr1 = {i:arr.count(i) for i in arr}
        arr1 = dict(sorted(arr1.items(), key=lambda item:item[1]))
        for key, val in arr1.items():
            while k > 0 and arr1[key] > 0:
                arr1[key]-=1
                k-=1
        return len([val for key, val in arr1.items() if val > 0])
        
# Solution 1 (104 ms, 32.2 MB)
