# Solution 1 (113 ms, 32.2 MB)

import numpy as np

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return np.max(np.sum(accounts, axis = 1))

# Solution 2 (86 ms, 14 MB)

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        arr = []
        for i in range(len(accounts)):
            val = sum(accounts[i])
            arr.append(val)
        return max(arr)

# Solution 3 (83 ms, 13.8 MB)

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(accounts[i]) for i in range(len(accounts))])