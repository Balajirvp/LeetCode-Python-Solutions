# Solution 1 (39 ms, 13.8 MB)

class Solution:
    def longestPalindrome(self, s: str) -> int:
        arr = Counter(s)
        lenn = [value for key, value in arr.items()]
        odd = [i for i in lenn if i % 2 == 1]
        even = [i for i in lenn if i % 2 == 0]
        if len(odd) > 0:
            return sum(even) + sum([i-1 for i in odd]) + 1
        else:
            return sum(even)