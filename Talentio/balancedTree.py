class Node(object):
    def __init__(self, value):
        self.data = value
        self.leftChild = None
        self.rightChild = None

    def preorderTraversal(self):
        print(self.data)
        if self.leftChild:
            self.leftChild.preorderTraversal()
        if self.rightChild:
            self.rightChild.preorderTraversal()

    def insertChild(self, child):
        t = child
        if t <= self.data:
            if self.leftChild:
                self.leftChild.insertChild(t)
            else:
                self.leftChild = Node(t)
        elif t > self.data:
            if self.rightChild:
                self.rightChild.insertChild(t)
            else:
                self.rightChild = Node(t)

    def isBalanced(self):
        if self.leftChild:
            if self.rightChild:
                return 1
            else:
                return 0
        elif self.rightChild:
            return 0
        else:
            return 1

root = Node(70)
root.insertChild(31)
root.insertChild(14)
root.insertChild(23)
root.insertChild(93)
root.insertChild(73)
root.insertChild(94)
root.preorderTraversal()

'''
k = root.isBalanced()
if k:
    if root.leftChild:
        if root.rightChild:
            a = root.leftChild.isBalanced()
            b = root.rightChild.isBalanced()
            if a and b:
                print(1)
            else:
                print(0)
        else:
            print(0)
    else:
        print(0)
else:
    print(0)'''
