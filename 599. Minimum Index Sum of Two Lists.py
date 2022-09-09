# Solution 1 (336 ms, 14.5 MB)

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        a = list(set(list1) & set(list2))
        dict1 = {}
        if len(a) == 1:
            return a
        else:
            for i in range(len(a)):
                dict1[a[i]] = list1.index(a[i]) + list2.index(a[i])
        return [k for k, v in dict1.items() if v == min(dict1.values())]

        