# Solution 1 (30 ms, 13.9 MB)

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        arr = Counter(text)
        dict1 = dict([(idx, val) if idx in 'ban' else (idx, val//2) for idx, val in arr.items() if idx in 'balon'])
        if len(dict1) == 5:
            return min(dict1.values())
        else:
            return 0
