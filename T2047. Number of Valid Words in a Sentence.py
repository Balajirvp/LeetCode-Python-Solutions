# Solution 1 (65 ms, 14.1 MB)

class Solution:
    def countValidWords(self, sentence: str) -> int:
        alpha = set('abcdefghijklmnopqrstuvwxyz-!.,')
        count = 0
        sent = sentence.split()
        for i in sent:
            if len(set(i) - alpha) == 0:
                if i.count('-') == 0 or (i.count('-') == 1 and 0 < i.index('-') < len(i) - 1 and i[i.index('-') - 1].islower() and i[i.index('-') + 1].islower()):
                    if i.count('!') + i.count('.') + i.count(',') == 0 or (i.count('!') + i.count('.') + i.count(',') == 1 and i[-1] in ('!', '.', ',')):   
                        count+=1
        return count

# Solution 2 (65 ms, 14.1 MB)

class Solution:
    def countValidWords(self, sentence: str) -> int:
        token_regex = re.compile(r'^([a-z]{1,}(\-[a-z]{1,})?[\.,!]?|[\.,!])$')
        return sum([1 for token in sentence.split()if re.search(token_regex, token)])