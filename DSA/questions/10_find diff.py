from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s) # {a:1,b:1,c:1,d:1}
        count_t = Counter(t) # {a:1,b:1,c:1,d:1,e:1}
        for i in count_t: # i will iterate through a , b ...
            if i not in count_s or count_s[i] < count_t[i]:
                return i