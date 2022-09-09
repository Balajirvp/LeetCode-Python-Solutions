# Solution 1 (53 ms, 14 MB)

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alpha = [chr(i) for i in range(97, 123)]
        num = [str(i) for i in range(1,27)]
        alphabets_dict = dict(zip(alpha, num))
        arr = []
        for i in s:
            arr.append(alphabets_dict[i])
        arr = list(''.join(arr))
        while k > 0:
            arr = list(str(sum([int(i) for i in arr])))
            k-=1
        return ''.join(arr)