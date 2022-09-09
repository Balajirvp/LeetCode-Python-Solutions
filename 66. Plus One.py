# Solution 1 (40 ms  13.8 MB)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      str_value = [str(i) for i in digits]
      int_value = int(''.join(str_value))
      fin_value = str(int_value+1)
      fin_list = []
      for i in range(len(fin_value)):
         fin_list.append(fin_value[i])
      return fin_list