# Solution 1 (45 ms, 13.8 MB)

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
        