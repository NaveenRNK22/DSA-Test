class Node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data

def Create(root,data):
    
    if root is None:
        return Node(data)
    elif root.data == data:
        return root
    elif root.data > data:
        root.right =  Create(root.right,data)
    else:
        root.left =  Create(root.left,data)
    return root

def PostOrder(root):
    if root is None:
        return
    PostOrder(root.left)
    PostOrder(root.right)
    print(root.data," ", end='')

r = Node(50)

r=Create(r,10)
r=Create(r,40)
r=Create(r,70)
r=Create(r,90)
r=Create(r,20)
r=Create(r,80)
r=Create(r,30)
r=Create(r,60)

print("The postorder Traversal output is")
PostOrder(r)
print("\n")