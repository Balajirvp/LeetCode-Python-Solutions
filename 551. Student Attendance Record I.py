# Solution 1 (56 ms, 13.8 MB)

class Solution:
    def checkRecord(self, s: str) -> bool:
        abs_count = sum(1 for i in s if i == 'A')
        late_count = [s[i:i+3] for i in range(len(s)) if len(s[i:i+3]) == 3 and set(s[i:i+3]) == {'L'}]
        return abs_count < 2 and len(late_count) == 0


# Solution 2 (41 ms, 13.8 MB)       

class Solution:
    def checkRecord(self, s: str) -> bool:
        return Counter(s)["A"] < 2 and "LLL" not in s 
        