# Solution 1 (742 ms, 13.9 MB)

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        arr = defaultdict(int)
        for i in range(lowLimit, highLimit + 1):
            summ = sum([int(j) for j in str(i)])
            arr[summ]+=1
        return max(arr.values())