# Solution 1 (40 ms, 14 MB)

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        arr = [i.lower() for i in re.split('(\W+)', paragraph) if i.isalpha() and i.lower() not in banned]
        arr1 = Counter(arr)
        arr2 = [key for key, val in arr1.items() if val == max(arr1.values())]
        return arr2[0]