Queue = [] # Array[0:99] of string
for i in range(100):
    Queue.append("")
QueueHead = -1
QueueTail = -1
NumberItems = 0

def Enqueue(Data):
    global Queue
    global QueueTail
    global NumberItems
    if NumberItems == 100:
        return False
    else:
        QueueTail += 1
        Queue[QueueTail] = Data
        NumberItems += 1
        return True

def Dequeue():
    global Queue
    global QueueHead
    global NumberItems
    if NumberItems == 0:
        return "False"
    else:
        QueueHead += 1
        NumberItems -= 1
        return Queue[QueueHead]

def ReadData():
    File = open("BinaryData.txt", "r")
    for line in File:
        Enqueue(line.strip())
    File.close()

def Compress():
    NewString = ""
    CurrentDigit = Dequeue()
    NextDigit = ""
    Count = 0
    while CurrentDigit != "False":
        NextDigit = Dequeue()
        if CurrentDigit == NextDigit:
            Count += 1
        else:
            NewString = NewString + CurrentDigit + str(Count)
            Count = 0
        CurrentDigit = NextDigit
    return NewString

ReadData()
String1 = Compress()
print(String1)