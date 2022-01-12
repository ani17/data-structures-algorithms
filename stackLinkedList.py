class Node:
    def __init__(self,d):
        self.data = d
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False

    def push(self,x):
        newNode = Node(x)
        if self.isEmpty():
            self.top = newNode
        else:
            temp = self.top
            newNode.next = temp
            self.top = newNode
    
    def pop(self):
        if self.isEmpty():
            print("Nothing to Pop")
            return
        else:
            temp = self.top
            self.top = temp.next
            del temp
    
    def stackTop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return
        else: 
            print('Top => ',self.top.data)
    
    def printStack(self):
        temp = self.top
        nodes = []
        while temp is not None:
            nodes.append(temp.data)
            temp = temp.next
        print(nodes)

s = Stack()
s.pop()
s.push('1')
s.printStack()
s.push('2')
s.push('3')
s.printStack()
s.stackTop()
s.pop()
s.printStack()
s.stackTop()
s.pop()
s.printStack()
s.stackTop()
