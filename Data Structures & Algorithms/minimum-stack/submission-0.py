from collections import deque
import heapq
class MinStack:

    def __init__(self):
        self.q = deque()
        self.mn = []

    def push(self, val: int) -> None:
        self.q.append(val)
        if self.mn:
            self.mn.append(min(self.mn[-1], val))
        else:
            self.mn.append(val)


    def pop(self) -> None:
        self.q.pop()
        self.mn.pop()

    def top(self) -> int:
        return self.q[-1]
        

    def getMin(self) -> int:
        return self.mn[-1]
