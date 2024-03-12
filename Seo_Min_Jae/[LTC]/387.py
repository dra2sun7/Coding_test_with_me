class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}

        for ch in s:
            if ch in dict:
                dict[ch] += 1
            else:
                dict[ch] = 1
        
        for i, ch in enumerate(s):
            if dict[ch] == 1:
                return i
        return -1

from collections import Counter

def first_unique_char_dic2(s: str) -> int:
    count = Counter(s)
    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i
    return -1