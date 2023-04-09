# Solution 1 (57 ms, 14.1 MB)

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowel = 'aeiou'
        cnt = 0
        for i in range(left, right+1):
            if words[i][0] in vowel and words[i][-1] in vowel:
                cnt+=1
        return cnt