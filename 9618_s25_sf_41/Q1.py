Queue = []
for i in range(20):
    Queue.append(-1)
HeadPointer = -1
TailPointer = -1
NumberItems = 0

def Enqueue(Item):
    global Queue
    global NumberItems
    global TailPointer
    if NumberItems == 20:
        return False
    else:
        TailPointer += 1
        Queue[TailPointer] = Item
        NumberItems += 1
        return True

def Dequeue():
    global NumberItems
    global Queue
    global HeadPointer
    if NumberItems == 0:
        return -1
    else:
        HeadPointer += 1
        NumberItems -= 1
        return Queue[HeadPointer]

for i in range(1, 26):
    if Enqueue(i):
        print(i, "Successful")
    else:
        print(i, "Unsuccessful")
print(Dequeue())
print(Dequeue())