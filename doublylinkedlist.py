class Node:
    def __init__(self,d):
        self.data = d
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self,nums):
        self.head = None
        nodes = {}
        # Prepare Link List
        if len(nums) > 0:
            for idx, num in enumerate(nums):
                nodes[idx] = Node(num)
            for idx in nodes:
                if idx == 0:
                    self.head = nodes[idx]
                    nodes[idx].prev = None
                    nodes[idx].next = nodes[idx+1]
                elif idx == len(nodes) - 1:
                    nodes[idx].prev = nodes[idx-1] 
                    nodes[idx].next = None
                else:
                    nodes[idx].prev = nodes[idx-1]
                    nodes[idx].next = nodes[idx+1]
    
    def printList(self):
        temp = self.head
        nodes = []
        while temp is not None:
            nodes.append(temp.data)
            temp = temp.next
        # print(nodes)
        print('-->'.join(nodes))
    
    def insertAtBeginning(self,x):
        newNode = Node(x)
        if self.head is not None:
            newNode.next = self.head
            newNode.prev = None
        self.head = newNode

    def insertAtPos(self,x,pos):
        newNode = Node(x)
        temp =self.head
        i = 1
        while temp is not None and temp.next is not None and i<=pos:
            temp = temp.next
            i += 1
        newNode.next = temp
        newNode.prev = temp.prev
        (temp.prev).next = newNode
    
    def insertAtEnd(self,x):
        newNode = Node(x)
        temp = self.head
        while temp is not None and temp.next is not None:
            temp = temp.next
        temp.next = newNode
        newNode.prev = temp
        newNode.next = None
    
    def deleteAtBeginning(self):
        if self.head is not None:
            temp = self.head
            (temp.next).prev = None
            self.head = temp.next
            del temp

    def deleteAtPos(self,pos):
        temp = self.head
        i = 1
        while temp is not None and temp.next is not None and i<=pos-1:
            temp = temp.next
            i += 1
        (temp.prev).next = temp.next
        (temp.next).prev = temp.prev
        del temp
    
    def deleteAtEnd(self):
        if self.head is not None:
            temp = self.head
            while temp is not None and temp.next is not None:
                temp = temp.next
            (temp.prev).next = None
            del temp
    
    def traverseBackwards(self):
        temp = self.head
        nodes = []
        while temp is not None and temp.next is not None:
            temp = temp.next
        while temp is not None:
            nodes.append(temp.data)
            temp = temp.prev

        print('-->'.join(nodes))

input_str = input('Enter the numbers:')
input_arr = input_str.split(' ')

dll = DoublyLinkedList(input_arr)
dll.printList()
dll.insertAtBeginning('100')
dll.printList()
dll.insertAtPos('500',2)
dll.printList()
dll.insertAtEnd('700')
dll.printList()
dll.deleteAtBeginning()
dll.printList()
dll.deleteAtPos(2)
dll.printList()
dll.deleteAtEnd()
dll.printList()
dll.traverseBackwards()
