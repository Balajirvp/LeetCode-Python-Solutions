# Solution 1 (29 ms, 13.9 MB)

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        w1 = 'aceg'
        w2 = 'bdfh'
        n1 = '2468'
        n2 = '1357'
        if (coordinates[0] in w1 and coordinates[1] in n1) or (coordinates[0] in w2 and coordinates[1] in n2):
            return True
        else:
            return False