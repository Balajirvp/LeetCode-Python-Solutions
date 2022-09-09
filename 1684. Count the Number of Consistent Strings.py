# Solution 1 (286 ms, 16.1 MB)

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        arr = set(allowed)
        count = 0
        for i in range(len(words)):
            if set(words[i]).issubset(arr):
                count+=1
        return count
                    