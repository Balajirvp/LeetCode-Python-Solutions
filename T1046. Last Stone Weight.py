# Solution 1 (35 ms, 13.8 MB)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            if len(stones) > 1:
                stones.sort()
                a = stones[-1] - stones[-2]
                stones.remove(stones[-1])
                stones.remove(stones[-1])
                if a > 0:
                    stones.append(a)
        return stones[0] if stones else 0
        
                                 
            