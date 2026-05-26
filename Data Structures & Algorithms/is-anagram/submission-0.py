from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter()
        for c in s:
            s_counter[c] += 1
        for c in t:
            s_counter[c] -= 1
            if s_counter[c] < 0:
                return False
        if s_counter.total() == 0:
            print(s_counter)
            return True
        return False        