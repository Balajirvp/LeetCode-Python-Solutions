# Solution 1 (35 ms, 13.9 MB)

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        dict1 = {
        'a': '.-',   'b': '-...', 'c': '-.-.', 'd': '-..',  'e': '.',    'f': '..-.', 'g': '--.',
        'h': '....', 'i': '..',   'j': '.---', 'k': '-.-',  'l': '.-..', 'm': '--',   'n': '-.',
        'o': '---',  'p': '.--.', 'q': '--.-', 'r': '.-.',  's': '...',  't': '-',    'u': '..-',
        'v': '...-', 'w': '.--',  'x': '-..-', 'y': '-.--', 'z': '--..'}

        return len(set([''.join([dict1[j] for j in i]) for i in words]))