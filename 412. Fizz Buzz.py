# Solution 1 (40 ms, 15 MB)

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        for i in range(1, n+1):
            if i % 15 == 0:
                arr.append('FizzBuzz')
            elif i % 3 == 0:
                arr.append('Fizz')
            elif i % 5 == 0:
                arr.append('Buzz')
            else:
                arr.append(str(i))
        return arr

# Solution 2 (39 ms, 15 MB)

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        f, b, fb = 'Fizz', 'Buzz', 'FizzBuzz'
        arr = [str(x + 1) for x in range(n)]
        
        for i in range(2, n, 3):
            arr[i] = f
        
        for i in range(4, n, 5):
            arr[i] = b
        
        for i in range(14, n, 15):
            arr[i] = fb
        
        return arr


# Solution 3 (48 ms, 15.1 MB)

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        dict1 = {3: 'Fizz', 5: 'Buzz'}
        divisors = [3, 5]
        for i in range(1, n+1):
            arr1 = []
            for key in divisors:
                if i % key == 0:
                    arr1.append(dict1[key])
            if not arr1:
                arr1.append(str(i))
            arr.append(''.join(arr1))
        return arr
