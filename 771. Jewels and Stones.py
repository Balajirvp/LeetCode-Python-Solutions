# Solution 1 (35 ms, 13.8 MB)

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone = Counter(stones)
        cnt = 0
        for i in jewels:
            cnt+=stone[i]
        return cnt