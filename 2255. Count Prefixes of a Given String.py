# Solution 1 (53 ms, 14.1 MB)

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        prefixes = [s[:i+1] for i in range(len(s))]
        return len([i for i in words if i in prefixes])

# Solution 2 (53 ms, 14.1 MB)

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return len([1 for word in words if word == s[:len(word)]]) 