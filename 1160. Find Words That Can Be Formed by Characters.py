# Solution 1 (192 ms, 14.6 MB)

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars1 = Counter(chars)
        count = 0
        for i in words:
            if Counter(i) <= chars1:
                count+=len(i)
        return count    
    
# Solution 2 (476 ms, 14.3 MB)

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = 0
        for i in words:
            if Counter(i) & Counter(chars) == Counter(i):
                cnt+=len(i)
        return cnt