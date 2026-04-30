class Node:
    def __init__(self, Data):
        self.LeftPointer = -1 # Integer
        self.Data = Data # Integer
        self.RightPointer = -1 # Integer

    def GetLeft(self):
        return self.LeftPointer

    def GetRight(self):
        return self.RightPointer

    def GetData(self):
        return self.Data

    def SetLeft(self, LeftPointer):
        self.LeftPointer = LeftPointer

    def SetRight(self, RightPointer):
        self.RightPointer = RightPointer

    def SetData(self, Data):
        self.Data = Data

class TreeClass:
    def __init__(self):
        self.Tree = [Node(-1)] # List Node
        self.FirstNode = -1 # Integer
        self.NumberNodes = 0 # Integer

    def InsertNode(self, NewNode):
        if self.NumberNodes == 0:
            self.Tree[self.NumberNodes] = NewNode
            self.NumberNodes += 1
            self.FirstNode = 0
        else:
            CurrentNode = self.Tree[self.FirstNode]
            self.Tree.append(NewNode)
            while CurrentNode.GetLeft() != -1 and CurrentNode.GetRight() != -1:
                if CurrentNode.GetData() > NewNode.GetData():
                    CurrentNode = self.Tree[CurrentNode.GetLeft()]
                elif CurrentNode.GetData() < NewNode.GetData():
                    CurrentNode = self.Tree[CurrentNode.GetRight()]
            if CurrentNode.GetData() > NewNode.GetData():
                CurrentNode.SetLeft(self.NumberNodes)
            elif CurrentNode.GetData() < NewNode.GetData():
                CurrentNode.SetRight(self.NumberNodes)
            self.NumberNodes += 1

    def OutputTree(self):
        if len(self.Tree) == 0:
            print("No nodes")
        else:
            for node in self.Tree:
                print(node.GetLeft(), node.GetData(), node.GetRight())

TheTree = TreeClass()
TheTree.InsertNode(Node(10))
TheTree.InsertNode(Node(11))
TheTree.InsertNode(Node(5))
TheTree.InsertNode(Node(1))
TheTree.InsertNode(Node(20))
TheTree.InsertNode(Node(7))
TheTree.InsertNode(Node(15))
TheTree.OutputTree()