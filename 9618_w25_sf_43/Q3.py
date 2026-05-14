def RecursiveCount(ArrayCopy, NumberElements, DataToFind):
    if len(ArrayCopy) == 0:
        return 0
    if ArrayCopy[0] == DataToFind:
        return 1 + RecursiveCount(ArrayCopy[1:], NumberElements, DataToFind)
    else:
        return RecursiveCount(ArrayCopy[1:], NumberElements, DataToFind)

Array1 = [0,5,1,2,5,9,9,6,5,0]
OutputValue = RecursiveCount(Array1, 10, 0)
print(OutputValue)

String1 = "x=0;y=1;x=x+y;y++;"

def SplitData(Data):
    Array = []
    String = ""
    for x in Data:
        if x != ";":
            String += x
        else:
            Array.append(String)
            String = ""
    return Array

ReturnedArray = SplitData(String1)
for i in ReturnedArray:
    print(i)