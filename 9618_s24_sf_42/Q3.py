NumberArray = [100, 85, 644, 22, 15, 8, 1]

def RecursiveInsertion(IntegerArray, NumberElements):
    if NumberElements <= 1:
        return IntegerArray
    else:
        RecursiveInsertion(IntegerArray, NumberElements - 1)
        LastItem = IntegerArray[NumberElements - 1]
        CheckItem = NumberElements - 2
    LoopAgain = True
    if CheckItem < 0:
        LoopAgain = False
    else:
        if IntegerArray[CheckItem] < LastItem:
            LoopAgain = False
    while LoopAgain:
        IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
        CheckItem = CheckItem - 1
        if CheckItem < 0:
            LoopAgain = False
        else:
            if IntegerArray[CheckItem] < LastItem:
                LoopAgain = False
    IntegerArray[CheckItem + 1] = LastItem
    return IntegerArray

def IterativeInsertion(IntegerArray, NumberElements):
    while NumberElements > 0:
        LastItem = IntegerArray[NumberElements - 1]
        CheckItem = NumberElements - 2
        LoopAgain = True
        if CheckItem < 0:
            LoopAgain = False
        elif IntegerArray[CheckItem] <= LastItem:
            LoopAgain = False
        while LoopAgain:
            IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
            CheckItem = CheckItem - 1
            if CheckItem < 0:
                LoopAgain = False
            elif IntegerArray[CheckItem] <= LastItem:
                LoopAgain = False
        IntegerArray[CheckItem + 1] = LastItem
        NumberElements = NumberElements - 1
    return IntegerArray

ReturnedArray = IterativeInsertion(NumberArray, len(NumberArray))
print("iterative")
print(ReturnedArray)