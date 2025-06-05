class Node():
    def __init__(self,data=None):
        self.data = data
        self.next = None
class LinkedList():
    def __init__(self):
        self.head = None
    def append(self,data):
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(data)
        else:
            self.head = Node(data)
    def reverse(self):
        curr,prev = self.head,None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr=temp
        self.head = prev

            
    def printlist(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next


        

linklist = LinkedList()
linklist.append(3)
linklist.append(4)

linklist2 = LinkedList()
linklist2.append(5)
linklist2.append(6)

dummy = first = linklist.head
while first.next:
    first =first.next
first.next = linklist2.head

while dummy:
    dummy = dummy.next

linklist.reverse()
linklist.printlist()

fast = linklist.head.next
slow = linklist.head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

print(slow.data)

second = slow
curr  = linklist.head
print("first half")
while second:
    print(curr.data)
    curr = curr.next
    
    second = second.next
    
