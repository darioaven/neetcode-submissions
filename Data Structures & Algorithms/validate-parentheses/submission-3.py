from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:

        q = deque()
        start = ["(", "{", "["]
        end = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        for c in s:
            if c in start:
                q.append(c)
            else:
                if not q:
                    return False
                val = q.pop()
                if end[c] != val:
                    return False
        if q:
            return False

        return not q
