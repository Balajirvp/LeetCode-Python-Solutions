# Solution 1 (291 ms, 14.4 MB)

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        subs = [word[i:j] for i in range(len(word)) for j in range(i+1, len(word)+1)]
        count = 0
        for i in subs:
            if len(set(i)) == 5 and sorted(set(i)) == ['a','e','i','o','u']:
                count+=1
        return count