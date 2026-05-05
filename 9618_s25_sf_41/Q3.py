class Node():
    def __init__(self, NodeData):
        self.NodeData = NodeData # Integer
        self.LeftNode = None # Node
        self.RightNode = None # Node

    def GetLeft(self):
        return self.LeftNode

    def GetRight(self):
        return self.RightNode

    def GetData(self):
        return self.NodeData

    def SetLeft(self, LeftNode):
        self.LeftNode = LeftNode

    def SetRight(self, RightNode):
        self.RightNode = RightNode

Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(5)
Node4 = Node(15)
Node5 = Node(7)

class Tree:
    def __init__(self, FirstNode):
        self.FirstNode = FirstNode