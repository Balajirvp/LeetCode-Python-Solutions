# Solution 1 (27 ms, 14 MB)

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        Alice1 = int(arriveAlice[-2:]) + sum(days[:int(arriveAlice[:2]) - 1])
        Alice2 = int(leaveAlice[-2:]) + sum(days[:int(leaveAlice[:2]) - 1])
        Bob1 = int(arriveBob[-2:]) + sum(days[:int(arriveBob[:2]) - 1])
        Bob2 = int(leaveBob[-2:]) + sum(days[:int(leaveBob[:2]) - 1])
        if Bob1 >= Alice1:
            if Bob1 > Alice2:
                return 0
            elif Bob2 <= Alice2:
                return Bob2 - Bob1 + 1
            else:
                return Alice2 - Bob1 + 1
        elif Alice1 >= Bob1:
            if Alice1 > Bob2:
                return 0
            elif Alice2 <= Bob2:
                return Alice2 - Alice1 + 1
            else:
                return Bob2 - Alice1 + 1