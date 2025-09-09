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

def height(root):
    leftHeight = 0
    rightHeight = 0
    
    if(root.left):
        leftHeight = height(root.left) + 1
    
    if(root.right):
        rightHeight = height(root.right) + 1
    
    if(leftHeight > rightHeight):
        return leftHeight
    else:
        return rightHeight

def InOrder(root):
    if root is None:
        return
    InOrder(root.left)
    print(root.data," ", end='')
    InOrder(root.right)


r=Node(50)

r=Create(r,10)
r=Create(r,40)
r=Create(r,70)
r=Create(r,90)
r=Create(r,20)
r=Create(r,80)
r=Create(r,30)
r=Create(r,60)

InOrder(r)
print("\nThe height of Tree is ",height(r))