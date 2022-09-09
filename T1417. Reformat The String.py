# Solution 1 (49 ms, 13.9 MB)

class Solution:
    def reformat(self, s: str) -> str:
        lett = [i for i in s if i.isalpha()]
        numb = [i for i in s if i.isnumeric()]
        l1 = len(lett)
        l2 = len(numb)
        if l1 == 1 and l2 == 0:
            return ''.join(lett)
        elif l1 == 0 and l2 == 1:
            return ''.join(numb) 
        elif l1 > 0 and l2 > 0 and abs(l1 - l2) <= 1:
            if l1 == l2:
                return ''.join([lett[i] + numb[i] for i in range(l1)])
            elif l1 > l2:
                arr =  ''.join([lett[i] + numb[i] for i in range(l2)])
                return arr + lett[-1]
            else:
                arr = ''.join([numb[i] + lett[i] for i in range(l1)])
                return arr + numb[-1]
        else:
            return ''

# Solution 2 (72 ms, 14 MB)

class Solution:
    def reformat(self, s: str) -> str:
        numb, lett = [d for d in s if d.isdigit()], [a for a in s if a.isalpha()]
        if abs(len(numb) - len(lett)) > 1: 
                return ''
        return [j for i in zip_longest(numb, lett) for j in i if j] if len(numb) > len (lett) else [j for i in zip_longest(lett, numb) for j in i if j]