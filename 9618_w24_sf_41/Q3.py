LinkedList = []
for i in range(20):
    if i == 19:
        LinkedList.append([-1,-1])
    else:
        LinkedList.append([-1, i+1])
FirstNode = -1
FirstEmpty = 0

def InsertData():
    