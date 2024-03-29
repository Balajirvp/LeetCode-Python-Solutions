# Solution 1 (103 ms, 13.9 MB)

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        cnt = 0
        for i in nums[:1:-1]:
            arr = [i - j for j in nums]
            arr = sum([(i - diff == 0 or i - diff == diff) for i in arr if i > 0])
            if arr == 2:
                cnt+=1
        return cnt

# Solution 2 (36 ms, 13.7 MB)

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        seen = set(nums)
        return sum(num - diff in seen and num - diff * 2 in seen for num in seen)