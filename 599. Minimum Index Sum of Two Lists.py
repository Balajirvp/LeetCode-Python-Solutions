# Solution 1 (223 ms, 16.7 MB)

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        arr = set(list1) & set(list2)
        val = {}
        for i in arr:
            val[i] = list1.index(i) + list2.index(i)
        num = min(val.values())
        return [i for i, v in val.items() if v == num] 

# Solution 2 (190 ms, 17 MB)

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        arr1 = {v:i for i, v in enumerate(list1)}
        arr2 = {v:i for i, v in enumerate(list2)}
        val = [i for i,v in (Counter(list1) + Counter(list2)).items() if v == 2]
        final = {}
        for i in val:
            final[i] = arr1[i] + arr2[i]
        num = min(final.values())
        return [i for i, v in final.items() if v == num] 
