# Solution 1 (29 ms, 13.8 MB)

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone = Counter(stones)
        jewel = list(jewels)
        count = 0
        for i in jewel:
            if i in stone:
                count+=stone[i]
        return count
        