# Solution 1 (253 ms, 14.4 MB)

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        subs = [word[i:j] for i in range(len(word)) for j in range(i+1, len(word)+1)]
        count = 0
        for i in subs:
            if len(set(i)) == 5 and sorted(set(i)) == ['a','e','i','o','u']:
                count+=1
        return count

# Solution 2 (312 ms, 14.4 MB)

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        cnt = 0
        arr = [word[i: i+k] for k in range(5, len(word) + 1) for i in range(0, len(word) - k + 1)]
        return sum(1 for i in arr if len(set('aeiou') - set(i)) == 0 and len(set(i)) == 5)
        