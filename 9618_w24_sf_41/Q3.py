LinkedList = []
for i in range(20):
    if i == 19:
        LinkedList.append([-1,-1])
    else:
        LinkedList.append([-1, i+1])
FirstNode = -1
FirstEmpty = 0

def InsertData():
    global LinkedList
    global FirstNode
    global FirstEmpty
    for i in range(5):
        item = int(input("Enter number: "))
        if LinkedList[FirstEmpty][0] != -1:
            break
        else:
            LinkedList[FirstEmpty][0] = item
            LinkedList[FirstEmpty][1] = FirstNode
            FirstNode += 1
            FirstEmpty += 1

def OutputLinkedList():
    global LinkedList
    global FirstNode
    CurrentNode = FirstNode
    while LinkedList[CurrentNode][1] != -1:
        print(LinkedList[CurrentNode][0])
        CurrentNode = LinkedList[CurrentNode][1]
    print(LinkedList[CurrentNode][0])

def RemoveData(target):
    global FirstNode
    global LinkedList
    found = False
    CurrentNode = FirstNode
    while not found:
        if LinkedList[CurrentNode][0] != target:
            CurrentNode = LinkedList[CurrentNode][1]
        else:
            found = True

InsertData()
OutputLinkedList()
RemoveData(5)
print("After")
OutputLinkedList()
