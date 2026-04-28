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
        self.Tree = [Node(-1)] # Node
        self.FirstNode = -1 # Integer
        self.NumberNodes = 0 # Integer

    def InsertNode(self, NewNode):
        if self.NumberNodes == 0:
            self.Tree[self.NumberNodes] = NewNode
            self.NumberNodes += 1
            self.FirstNode = 0
        else:
            CurrentNode = self.Tree[self.FirstNode]
            while CurrentNode.LeftPointer == -1 and CurrentNode.RightPointer == -1:
                if CurrentNode.Data > NewNode.Data:
                    CurrentNode = self.Tree[CurrentNode.LeftPointer]
                    if CurrentNode.LeftPointer == -1:
                        CurrentNode.LeftPointer = self.NumberNodes
                elif CurrentNode.Data < NewNode.Data:
                    CurrentNode = self.Tree[CurrentNode.RightPointer]
                    if CurrentNode.RightPointer == -1:
                        CurrentNode.RightPointer = self.NumberNodes
            self.NumberNodes += 1

    def OutputTree(self):
        if len(self.Tree) == 0:
            print("No nodes")
        else:
            for node in self.Tree:
                print(node)

TheTree = TreeClass()
