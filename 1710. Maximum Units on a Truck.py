# Solution 1 (711 ms, 26.5 MB)

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        arr = [[i[1]]*i[0] for i in boxTypes]
        arr2 = [j for i in arr for j in i]
        arr2.sort(reverse = True)
        return sum(arr2[:truckSize])
    