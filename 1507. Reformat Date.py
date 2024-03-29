# Solution 1 (31 ms, 13.9 MB)

class Solution:
    def reformatDate(self, date: str) -> str:
        arr = date.split()
        month = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr':'04', 'May':'05', 'Jun':'06', 'Jul':'07', 'Aug': '08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
        l = len(arr[0])
        day = '0' + arr[0][0] if l == 3 else arr[0][:2]
        return arr[-1] + '-' + month[arr[1]] + '-' + day

# Solution 2 (27 ms, 13.8 MB)  

class Solution:
    def reformatDate(self, date: str) -> str:
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        arr = date.split()
        return '-'.join( ( arr[-1], str(months.index(arr[1]) + 1).rjust(2, "0"), arr[0][:-2].rjust(2, "0") ) )