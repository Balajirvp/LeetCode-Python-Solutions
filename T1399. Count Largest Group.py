# Solution 1 (168 ms, 14.3 MB)

class Solution:
    def countLargestGroup(self, n: int) -> int:
        sum_dict = defaultdict(list)
        for i in range(1, n+1):
            summ = 0
            res = [int(j) for j in str(i)]
            summ+=sum(res)
            sum_dict[summ].append(i)
        res = [len(v) for i,v in sum_dict.items()]
        return sum(1 for i in res if i == max(res))