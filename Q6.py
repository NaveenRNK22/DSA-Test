class Node:

    def __init__(self,data):
        self.next = None
        self.data = data
    
class LinkedList:

    def __init__(self):
        self.head = None

    def create(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
            
        
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            
            cur.next = new_node
        

def printll(head):
    if head == None:
        return None
    
    cur = head
    while cur:
        print(cur.data)
        cur = cur.next

def reverse(head):
    cur = head
    prev = None
    while cur:
        nex = cur.next
        cur.next = prev
        prev = cur
        cur = nex

    return prev

Ll = LinkedList()
arr = list(map(int,input("Enter the value to be inserted in Linked List:").split()))

for i in arr:
    Ll.create(i)
print("The output of the Linked List:\n")
printll(Ll.head)
print("The output after Reversing the Linked List:\n")
Ll.head = reverse(Ll.head)
printll(Ll.head)