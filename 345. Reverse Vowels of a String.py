# Solution 1 (44 ms, 15.6 MB)

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [i for i in s if i in 'aeiouAEIOU'][::-1]
        s = list(s)
        j = 0
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                s[i] = vowels[j]
                j+=1
        return ''.join(s)

# Solution 2 (52 ms, 18.4 MB)

class Solution:
    def reverseVowels(self, s: str) -> str:
        a = [idx for idx, val in enumerate(s) if val in 'aeiouAEIOU']
        b = [val for idx, val in enumerate(s) if val in 'aeiouAEIOU'][::-1]
        dict1 = dict(zip(a,b))
        arr = list(s)
        for i,v in dict1.items():
            arr[i] = v
        return ''.join(arr)