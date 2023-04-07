# Solution 1 (34 ms, 13.8 MB)

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        a = Counter(''.join(key.split()))
        keys = [k for k,v in a.items()]
        alphabets = [chr(i) for i in range(97,123)]
        final = dict(zip(keys, alphabets))
        arr = []
        for i in message:
            if i == ' ':
                arr.append(' ')
            else:
                arr.append(final[i])
        return ''.join(arr)
    
# Solution 2 (34 ms, 13.8 MB)

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dict1, arr = {}, []
        num = 97
        for i in list(key):
            if ord(i) >= num and ord(i) < num + 26:
                if i not in dict1:
                    dict1[i] = chr(num)
                    num+=1
        for i in list(message):
            arr.append(dict1.get(i, ' '))
        return ''.join(arr)