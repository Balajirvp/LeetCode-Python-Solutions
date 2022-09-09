# Solution 1 (72 ms  20 MB)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        final_s = [i.lower() for i in s if i.isalnum() is True]
        return final_s == final_s[::-1]

# Solution 2 (72 ms  14.3 MB)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        
        while left < right:
           while left < right and not s[left].isalnum():
              left+= 1
           while left < right and not s[right].isalnum():
              right-= 1
            
           if s[left].lower() != s[right].lower():
              return False
            
           left+= 1
           right-= 1
           
        return True
