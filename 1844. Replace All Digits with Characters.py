# Solution 1 (42 ms, 13.9 MB)

class Solution:
    def replaceDigits(self, s: str) -> str:
        arr = [chr(i) for i in range(97, 123)]
        dict1 = {val:idx for idx, val in enumerate(arr)}
        s = list(s)
        for i in range(1, len(s), 2):
            s[i] = arr[dict1[s[i-1]] + int(s[i])]
        return ''.join(s)

# Solution 2 (26 ms, 13.9 MB)

class Solution:
    def replaceDigits(self, s: str) -> str:
        arr = []
        for idx, val in enumerate(s):
            if ord(val) >= 97 and ord(val) <= 122:
                arr.append(val)
            else:
                arr.append(chr(int(val) + ord(s[idx - 1])))
        return ''.join(arr)
        
       