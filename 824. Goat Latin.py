# Solution 1 (32 ms, 13.9 MB)

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sent = tuple(sentence.split())
        arr = []
        for i in range(len(sent)):
            if sent[i][0] in 'aeiouAEIOU':
                j = sent[i] + 'ma' + 'a'*(i+1)
                arr.append(j)
            else:
                j = sent[i][1:] + sent[i][0] + 'ma' + 'a'*(i+1)
                arr.append(j)
        return ' '.join(arr)