# Solution 1 (427 ms, 20.3 MB)

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        dict1 = {'type': 0, 'color': 1, 'name': 2}
        count = 0
        for i in range(len(items)):
            if items[i][dict1[ruleKey]] == ruleValue:
                count+=1
        return count