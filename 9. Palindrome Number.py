# Solution 1 (66 ms  13.9 MB)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]