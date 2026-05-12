Queue = [] # Array[0:99] of string
for i in range(100):
    Queue.append("")
QueueHead = -1
QueueTail = -1
NumberItems = 0

def Enqueue(Data):
    global Queue
    global QueueHead
    global QueueTail
    global NumberItems
    if NumberItems == 100:
        return False
    elif QueueHead == -1:
        QueueHead += 1
        QueueTail += 1
        Queue[QueueTail] = Data
        NumberItems += 1
    
