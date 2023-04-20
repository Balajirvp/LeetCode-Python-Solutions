# Solution 1 (36 ms, 13.8 MB)

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
        return int(''.join(arr))

# Solution 2 (36 ms, 13.8 MB)

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        convert = ''.join([str(ord(i) - 96) for i in s])
        while k > 0:
            a = sum(int(i) for i in convert)
            convert = [i for i in str(a)]
            k-=1
        return int(''.join(convert))