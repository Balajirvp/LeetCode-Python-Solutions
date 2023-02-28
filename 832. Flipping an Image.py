# Solution 1 (246 ms, 32 MB)

import numpy as np

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        arr = np.array(image)
        return 1- arr[:,::-1]
        
# Solution 2 (256 ms, 32.1 MB)

import numpy as np

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        arr = np.array(image)
        return 1 - np.flip(arr, axis = 1)
        
# Solution 3 (62 ms, 13.9 MB)

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        lenn = len(image)
        arr = [[[0] for i in range(lenn)] for i in range(lenn)]
        for i in range(len(image)):
            for j in range(len(image[i])):
                arr[i][j] = image[i][lenn - j - 1]
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == 1:
                    arr[i][j] = 0
                else:
                    arr[i][j] = 1
        return arr
        
# Solution 4 (59 ms, 14 MB)

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        arr = []
        for i in range(len(image)):
            arr.append(image[i][::-1])
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == 1:
                    arr[i][j] = 0
                else:
                    arr[i][j] = 1
        return arr

# Solution 5 (47 ms, 13.8 MB)       

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        arr = [i[::-1] for i in image]
        arr1 = [1 - j for i in arr for j in i]
        n = len(image)
        return [arr1[i:i+n] for i in range(0, len(arr1), n)]