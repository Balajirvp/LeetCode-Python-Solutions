# Solution 1 (31 ms, 13.8 MB) (Better solution)

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = 'aeiouAEIOU'
        l = len(s)
        cnt1, cnt2 = 0, 0
        arr1, arr2 = s[:l//2], s[l//2:]
        for i in vowels:
            cnt1+=arr1.count(i)
            cnt2+=arr2.count(i)
        return cnt1 == cnt2

# Solution 2 (45 ms, 13.8 MB)

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        a = list(s)
        l = int(len(a)/2)
        arr1 = a[:l]
        arr2 = a[l:]
        cnt1 = 0
        cnt2 = 0
        for i in arr1:
            if i in vow:
                cnt1+=1
        for i in arr2:
            if i in vow:
                cnt2+=1
        return cnt1 == cnt2
    

        
        