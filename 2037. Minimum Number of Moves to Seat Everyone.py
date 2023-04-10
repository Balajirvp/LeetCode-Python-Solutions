# Solution 1 (265 ms, 32 MB)

import numpy as np

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return np.sum(np.abs(np.array(sorted(students)) - np.array(sorted(seats))))

# Solution 2 (58 ms, 13.8 MB)

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        return sum([abs(seats[i] - students[i]) for i in range(len(seats))])
        