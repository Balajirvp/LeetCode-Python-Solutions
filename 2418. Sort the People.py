# Solution 1 (105 ms, 14.4 MB)

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        arr = sorted((zip(names, heights)), key = lambda x:x[1], reverse = True)
        return [i[0] for i in arr]