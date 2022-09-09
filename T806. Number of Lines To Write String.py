# Solution 1 (57 ms, 13.9 MB)

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        let = [chr(i) for i in range(97,123)]
        lett = dict(zip(let, widths))
        line, width = 1, 0
        for i in s:
            w = lett[i]
            width+=w
            if width > 100:
                line+=1
                width = w
        return line, width