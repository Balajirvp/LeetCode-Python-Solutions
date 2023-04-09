# Solution 1 (22 ms, 13.9 MB)  

class Solution:
    def freqAlphabets(self, s: str) -> str:
        # dict1 = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10#': 'j', '11#': 'k', '12#': 'l', '13#': 'm', '14#': 'n', '15#': 'o', '16#': 'p', '17#': 'q', '18#': 'r', '19#': 's', '20#': 't', '21#': 'u', '22#': 'v', '23#': 'w', '24#': 'x', '25#': 'y', '26#': 'z'}
        dict1 = {str(i):chr(96 +i) for i in range(1,10)} | {str(i) +'#':chr(96 + i) for i in range(10,27)}
        arr = []
        idx = 0
        while idx < len(s):
            if idx + 2 < len(s) and s[idx + 2] == '#':
                arr.append(dict1[s[idx:idx + 3]])
                idx += 3
            else:
                arr.append(dict1[s[idx]])
                idx += 1
        return ''.join(arr)


# Solution 1 (48 ms, 13.9 MB)   

# class Solution:
#     def freqAlphabets(self, s: str) -> str:
#         char = [chr(i) for i in range(97,123)]
#         nums = [int(i) for i in range(1,27)]
#         arr = dict(zip(nums, char))      
#         i = 0
#         l = len(s)
#         res = []
#         while i < l:
#             if i < l- 2 and s[i+2] == '#':
#                 res.append(arr[int(s[i:i+2])])
#                 i+=3
#             else:
#                 res.append(arr[int(s[i])])
#                 i+=1
#         return ''.join(res)

# Solution 2 (87 ms, 14 MB)

# class Solution:
#     def freqAlphabets(self, s: str) -> str:
#         first = [chr(i) for i in range(97,106)]
#         first_num = [str(i) for i in range(1,10)]
#         last = [chr(i) for i in range(106,123)]
#         last_num = [str(i) + '#' for i in range(10,27)]
#         dict1 = dict(zip(first_num, first))
#         dict2 = dict(zip(last_num, last))
#         dict1.update(dict2)
        
#         r1 = [i for i,v in enumerate(s) if v == '#']
#         r2 = []
#         for i in range(len(s)):
#             if i in r1:
#                 r2.append(s[i-2:i+1])
#             elif i < len(s) - 2 and s[i+1] != '#' and s[i+2] != '#' and s[i] != '#':
#                 r2.append(s[i])
#             continue      
#         if s[-2] != '#' and s[-1] != '#':
#             r2.append(s[-2])
#         if s[-1] != '#':
#             r2.append(s[-1])
#         res = []
#         for i in r2:
#             res.append(dict1[i])
#         return ''.join(res)

# Misc stuff

# class Solution:
#     def freqAlphabets(self, s: str) -> str:
#         dict1 = {str(i):chr(96 +i) for i in range(1,10)} | {str(i)+'#':chr(96 + i) for i in range(10,27)}
#         idxs = [idx for idx, val in enumerate(s) if val == '#']
#         arr = []
#         a = s
#         for i in idxs:
#             arr.append(s[i - 2:i + 1])
#             a = a.replace(s[i - 2:i + 1], '')
#         a = [i for i in a]
#         arr.extend(a)
#         return ''.join([dict1[i] for i in arr])
        
            
        
        
            
        
        