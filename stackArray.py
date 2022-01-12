class Stack:
    def __init__(self,s):
        self.size = s
        self.top = -1
        self.A = [None] * s

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    def push(self,x):
        if self.top + 1 > (self.size - 1):
            print("Stack Overflow")
            return
        else:
            print("Pushed ",x)
            self.top += 1
            self.A[self.top] = x
    
    def pop(self):
        if self.isEmpty():
            print("Nothing to Pop. Stack Empty")
        else:
            self.top -= 1

    def stackTop(self):
        print("Top => ", self.A[self.top])

    def printStack(self):
        print("Stack => ", self.A)


s = Stack(10)
s.printStack()
s.pop()
s.printStack()
s.push(100)
s.push(200)
s.stackTop()
s.push(300)
s.stackTop()
s.pop()
s.stackTop()
s.pop()
s.stackTop()
s.pop()
s.stackTop()
