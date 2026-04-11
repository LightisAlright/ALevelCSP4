from collections.abc import Hashable


class NewRecord:
    def __init__(self, Key, Item1, Item2):
        self.Key = Key #integer
        self.Item1 = Item1 #integer
        self.Item2 = Item2 #integer

HashTable = []
Spare = []

def Initialise():
    global HashTable
    global Spare
    for i in range(200):
        HashTable.append(NewRecord(-1, -1, -1))
    for i in range(100):
        Spare.append(NewRecord(-1, -1, -1))

def CalculateHash(Key):
    HashValue = Key % 200
    return HashValue

def InsertIntoHash(Record):
    global HashTable
    global Spare
    HashValue = CalculateHash(Record.Key)
    if HashTable[HashValue].Key == -1:
        HashTable[HashValue] = Record
    else:
        index = 0
        while Spare[index].Key != -1:
            index += 1
        Spare[index] = Record

def CreateHashTable():
    file = open("HashData.txt", "r")
    Values = []
    for line in file:
        Values.append(line.split(","))
    for Record in Values:
        InsertIntoHash(NewRecord(int(Record[0]), int(Record[1]), int(Record[2])))
    file.close()

def PrintSpare():
    global Spare
    index = 0
    while Spare[index].Key != -1:
        print(Spare[index].Key)
        index += 1

Initialise()
CreateHashTable()
PrintSpare()