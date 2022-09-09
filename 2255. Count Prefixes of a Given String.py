# Solution 1 (88 ms, 14.1 MB)

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        s_list = [s[0:0+j] for j in range(1,len(s)+1)]
        return len([i for i in words if i in s_list])

# Solution 2 (72 ms, 14.1 MB)

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return len([1 for word in words if word == s[:len(word)]]) 