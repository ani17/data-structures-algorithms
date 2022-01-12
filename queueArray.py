class Queue:
    def __init__(self,s):
        self.front = -1
        self.rear = -1
        self.A = [None] * s

    def isEmpty(self):
        if self.front == -1 and self.rear == -1:
            return True
        else:
            return False
    
    def enqueue(self,x):
        if self.rear + 1 > len(self.A) - 1:
            print("Queue Full")
            return
        else:
            if self.isEmpty():
                self.front += 1
            
            self.rear += 1
            self.A[self.rear] = x
            print("Enqueue", x)
    
    def dequeue(self):
        if self.isEmpty() or self.front == self.rear:
            print("Queue Empty. Nothing to Dequeue")
        else:
            print("Dequeue", self.A[self.front])
            self.front += 1

    def printQueue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("F =>", self.front, "Rear =>" ,self.rear)
            print("Queue => ", self.A[self.front : self.rear])

q = Queue(10)
q.printQueue()
for i in range(1,12):
    # print(i)
    q.enqueue(i)
q.printQueue()
for i in range(11):
    q.dequeue()
    q.printQueue()
