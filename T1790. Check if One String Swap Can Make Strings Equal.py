# Solution 1 (40 ms, 13.9 MB)

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        a = list(zip(s1,s2))
        summ = sum(1 for i in range(len(a)) if len(set(a[i][0]) - set(a[i][1])) != 0)
        if l1 == l2 and sorted(Counter(s1).items()) == sorted(Counter(s2).items()) and (summ == 0 or summ == 2):
            return True
        else:
            return False

# Solution 2 (34 ms, 13.8 MB)

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        elif sorted(Counter(s1).items()) == sorted(Counter(s2).items()):
            cnt = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    cnt+=1
            return cnt <= 2
        else:
            return False