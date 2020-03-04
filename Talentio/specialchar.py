class Node(object):
    def __init__(self,value):
        self.data = value
        self.leftChild = None
        self.rightChild = None

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

    def findElement(self,item):
        searchFor = item
        if searchFor == self.data:
            print("Your item is found")
        elif searchFor <= self.data:
            if self.leftChild:
                self.leftChild.findElement(searchFor)
            else:
                print("Not found")
        elif searchFor > self.data:
            if self.rightChild:
                self.rightChild.findElement(searchFor)
            else:
                print("Not found")

def preOrder(self):
        print(self.data, end=" ")
        if self.leftChild:
            self.leftChild.preOrder()
        if self.rightChild:
            self.rightChild.preOrder()

def inOrder(self):
        if self.leftChild:
            self.leftChild.inOrder()
        print(self.data, end=" ")
        if self.rightChild:
            self.rightChild.inOrder()

def postOrder(self):
        if self.leftChild:
            postOrder(self.leftChild)
        if self.rightChild:
            postOrder(self.rightChild)
        print(self.data, end=" ")


root = Node(70)

root.insertChild(31)
root.insertChild(14)
root.insertChild(23)
root.insertChild(93)
root.insertChild(73)
root.insertChild(94)

root.findElement(32)

#root.preOrder()

#root.inOrder()

postOrder(root)







