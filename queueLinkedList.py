class Node:
    def __init__(self,d):
        self.data = d
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def isEmpty(self):
        if self.front is None and self.rear is None:
            return True
        else:
            return False
    
    def enqueue(self,x):
        newNode = Node(x)
        
        if self.isEmpty():
            self.front = newNode
            self.rear = newNode
        else:
            (self.rear).next = newNode
            self.rear = newNode
    
    def dequeue(self):
        if self.isEmpty():
            print("Nothing to Dequeue")
            return
        else:
            temp = self.front
            if self.front == self.rear:
                self.front = self.rear = None
            else:
                self.front = temp.next
            print('dequeuing',temp.data)
            del temp
    
    def traverse(self):
        temp = self.front
        nodes = []
        if self.isEmpty():
            print('Queue is Empty')
        else:
            while temp is not None:
                nodes.append(temp.data)
                temp = temp.next
            print('-->'.join(nodes))

q = Queue()
q.traverse()
q.enqueue('1')
q.enqueue('2')
q.enqueue('3')
q.traverse()
q.dequeue()
q.traverse()
q.dequeue()
q.traverse()
q.dequeue()
q.traverse()
q.dequeue()