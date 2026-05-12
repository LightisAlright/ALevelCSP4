class BoardObject:
    def __init__(self, Code, Value):
        self.Code = Code # String
        self.Value = Value # Integer

    def GetCode(self):
        return self.Code

    def GetValue(self):
        return self.Value

Object1 = BoardObject("A", 2)
Object2 = BoardObject("B", 3)
Object3 = BoardObject("C", 5)
Object4 = BoardObject("D", 2)
Object5 = BoardObject("E", 7)

class Board:
    def __init__(self):
        self.TheBoard = [] # Array[0:9. 0:9] of BoardObject
        for i in range(10):
            self.TheBoard.append([])
            for j in range(10):
                self.TheBoard[i].append(BoardObject("-", 0))

    def GetObject(self, Row, Column):
        return self.TheBoard[Row][Column]

    def SetObject(self, Object, Row, Column):
        self.TheBoard[Row][Column] = Object

    def DisplayBoard(self):
        for i in range(10):
            for j in range(10):
                print(self.GetObject(i, j).GetCode(), end=" ")
            print("\t")

Board1 = Board()
Board1.SetObject(Object1, 0, 0)
Board1.SetObject(Object2, 9, 9)
Board1.SetObject(Object3, 4, 5)
Board1.SetObject(Object4, 2, 2)
Board1.SetObject(Object5, 8, 7)
Board1.DisplayBoard()

RowPos = -1
ColumnPos = -1
while RowPos < 0 or RowPos > 9:
    try:
        RowPos = int(input("Input row position: "))
    except ValueError:
        pass
while ColumnPos < 0 or ColumnPos > 9:
    try:
        ColumnPos = int(input("Input row position: "))
    except ValueError:
        pass
if Board1.GetObject(RowPos, ColumnPos).GetCode() == "-":
    print("Miss")
else:
    print(f"Code: {Board1.GetObject(RowPos, ColumnPos).GetCode()}, Value: {Board1.GetObject(RowPos, ColumnPos).GetValue()}")