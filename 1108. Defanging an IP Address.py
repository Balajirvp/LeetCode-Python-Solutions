# Solution 1 (58 ms, 13.8 MB)

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')

# Solution 2 (47 ms, 13.9 MB)

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return '[.]'.join(address.split('.'))