# Solution 1 (1453 ms, 15.5 MB)

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        l1 = len(s)
        for i in g:
            for j in s:
                if j - i >= 0:
                    s.remove(j)
                    break
        l2 = len(s)
        return l1-l2

# Solution 2 (187 ms, 15.8 MB)

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i=j=0
        ans=0
        while i<len(s) and j<len(g):
            if s[i]>=g[j]:
                ans+=1
                i+=1
                j+=1
            else:
                i+=1
        return ans