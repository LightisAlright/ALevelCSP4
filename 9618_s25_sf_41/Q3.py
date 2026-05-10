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

class Tree:
    def __init__(self, FirstNode):
        self.FirstNode = FirstNode # Node

    def GetrootNode(self):
        return self.FirstNode

    def Insert(self, NewNode):
        CurrentNode = self.FirstNode
        while CurrentNode.GetLeft() != None and  CurrentNode.GetRight() != None:
            if CurrentNode.GetData() > NewNode.GetData():
                CurrentNode = CurrentNode.GetLeft()
            elif CurrentNode.GetData() < NewNode.GetData():
                CurrentNode = CurrentNode.GetRight()
        if CurrentNode.GetData() > NewNode.GetData():
            CurrentNode.SetLeft(NewNode)
        elif CurrentNode.GetData() < NewNode.GetData():
            CurrentNode.SetRight(NewNode)

def OutputInOrder(TargetNode):
    if TargetNode.GetLeft() != None:
        OutputInOrder(TargetNode.GetLeft())
    print(TargetNode.GetData())
    if TargetNode.GetRight() != None:
        OutputInOrder(TargetNode.GetRight())

Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(5)
Node4 = Node(15)
Node5 = Node(7)

Tree1 = Tree(Node1)
Tree1.Insert(Node2)
Tree1.Insert(Node3)
Tree1.Insert(Node4)
Tree1.Insert(Node5)
OutputInOrder(Tree1.GetrootNode())