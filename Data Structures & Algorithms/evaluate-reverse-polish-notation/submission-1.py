from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        q = deque()
        signs = ["+", "-", "*", "/"]
        for t in tokens:
            
            if t in signs:
                v1 = int(q.pop())
                v2 = int(q.pop())
                if t == "+":
                    q.append(v1 + v2)
                elif t == "-":
                    q.append(v2 - v1)
                elif t == "*":
                    q.append(v2 * v1)
                else:
                    q.append(int(v2 / v1))
            else:
                q.append(t)
        return int(q.pop())
