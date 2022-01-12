class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class LinkedList:
    def __init__(self, nums):
        self.head = None
        nodes = {}

        # Create New nodes
        if len(nums) > 0:
            for idx, num in enumerate(nums):
                nodes[idx] = Node(num)
        
        # Create links
        for idx in nodes:
            if idx == 0:
                self.head = nodes[idx]
                nodes[idx].next = nodes[idx + 1]
            elif idx == len(nodes) - 1:
                nodes[idx].next = None
            else:
                nodes[idx].next = nodes[idx + 1]
            
            # print(nodes[idx].data, nodes[idx].next)
    
    def traverse(self):
        temp = self.head
        listItems = []
        while(temp is not None):
            listItems.append(temp.data)
            temp = temp.next
        
        print("-->".join(listItems))

    def insertAtBeginning(self,x):
        newNode = Node(x)
        newNode.next = self.head
        self.head = newNode

    def deleteAtBeginning(self):
        temp = None
        temp = self.head # point to node pointed by head
        self.head = temp.next # change head to point to node next to head
        del temp # delete node at beginning
    
    def insertAtEnd(self,x):
        newNode = Node(x) # Create
        temp = None
        temp = self.head
        while temp is not None and temp.next is not None: # Traverse till end
            temp = temp.next
        temp.next = newNode # Add
    
    def deleteAtEnd(self):
        temp = None
        temp = self.head
       
        # Traverse till second last node
        while (temp.next).next is not None:
            temp = temp.next
        
        lastNode = temp.next # Always keep node to be deleted in variable 
        temp.next = None
        del lastNode
    
    def insertAtPos(self, x, pos):
        newNode = Node(x)
        temp = self.head
        i = 1
        # Traverse till pos-1 node
        while temp is not None and temp.next is not None and i < pos-1:
            temp = temp.next
            i += 1
        newNode.next = temp.next
        temp.next = newNode
    
    def deleteAtPos(self,pos):
        temp = None
        temp = self.head
        i = 1
        while temp is not None and temp.next is not None and i < pos-1:
            temp = temp.next
            i += 1
        delNode = temp.next  # Always keep node to be deleted in variable
        temp.next = (temp.next).next
        del(delNode)

    
user_input = input('Enter the values space separated:')
user_input_arr = user_input.split(' ')

ll = LinkedList(user_input_arr)
ll.traverse()
ll.insertAtBeginning('100')
ll.traverse()
ll.deleteAtBeginning()
ll.traverse()
ll.insertAtEnd('500')
ll.traverse()
ll.deleteAtEnd()
ll.traverse()
ll.insertAtPos('600',3)
ll.traverse()
ll.deleteAtPos(2)
ll.traverse()
