# Solution 1 (121 ms, 13.8 MB)

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and (i*j) % k == 0:
                    count+=1
        return count

# Solution 2 (89 ms, 13.8 MB)

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        table, count = {}, 0
        for idx in range(len(nums)):
            if nums[idx] not in table:
                table[nums[idx]] = []
            for i in table[nums[idx]]:
                if (i*idx) % k == 0:
                    count += 1
            table[nums[idx]].append(idx)
        return count   