
class MyQueue:

    def __init__(self):
        self.s1 = [] # stack 1
        self.s2 = [] # stack 2

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if self.s2:
            return self.s2.pop()

        while self.s1:
            self.s2.append(self.s1.pop())

        if self.s2:
            return self.s2.pop()
        else:
            return

    def peek(self) -> int:
        if self.s2:
            return self.s2[0]

        while self.s1:
            self.s2.append(self.s1.pop())

        if self.s2:
            return self.s2[0]
        else:
            return



    def empty(self) -> bool:
        return not self.s1 and not self.s2
