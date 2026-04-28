class Queue:
    def __init__(self, Headpointer, Tailpointer):
        self.QueueArray = [] # array of integers
        self.Headpointer = Headpointer # integer
        self.Tailpointer = Tailpointer # integer

TheQueue = Queue(-1,0)
for i in range(100):
    TheQueue.QueueArray.append(-1)

def Enqueue(AQueue, TheData):
    if AQueue.Headpointer == -1:
        AQueue.QueueArray[AQueue.Tailpointer] = TheData
        AQueue.Headpointer = 0
        AQueue.Tailpointer = AQueue.Tailpointer + 1
        return 1
    else:
        if AQueue.Tailpointer > 100:
            return 1
        else:
            AQueue.QueueArray[AQueue.Tailpointer] = TheData
            AQueue.Tailpointer = AQueue.Tailpointer + 1
            return 1

def ReturnAllData():
    global TheQueue
    index = TheQueue.Headpointer
    ReturnedString = str(TheQueue.QueueArray[index])
    index += 1
    while index < TheQueue.Tailpointer:
        ReturnedString = ReturnedString + " " + str(TheQueue.QueueArray[index])
        index += 1
    return ReturnedString

word_count = 0
while word_count != 10:
    try:
        number = int(input("Enter a number (>0): "))
    except ValueError:
        continue
    if number < 0:
        continue
    else:
        if Enqueue(TheQueue, number) == -1:
            print("the queue is full")
        else:
            print(f"{number} has been added to the queue")
        word_count += 1
print(ReturnAllData())

def Dequeue():
    global TheQueue
    if TheQueue.Headpointer == TheQueue.Tailpointer - 1:
        return -1
    else:
        output = TheQueue.QueueArray[TheQueue.Headpointer]
        TheQueue.Headpointer = TheQueue.Headpointer + 1
        return output

for i in range(2):
    output = Dequeue()
    if output == -1:
        print("Queue empty")
    else:
        print(output)
print(ReturnAllData())
