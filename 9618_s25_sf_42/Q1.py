Stack = []
for i in range(20):
    Stack.append("-1")
TopOfStack = -1

def Push(Data):
    global TopOfStack
    global Stack
    if TopOfStack == 19:
        return -1
    else:
        TopOfStack += 1
        Stack[TopOfStack] = Data
        return 1

def Pop():
    global TopOfStack
    global Stack
    if TopOfStack == -1:
        return "-1"
    else:
        ReturnValue = Stack[TopOfStack]
        TopOfStack -= 1
        return ReturnValue

def ReadData(filename):
    global TopOfStack
    global Stack
    try:
        file = open(filename)
        for line in file:
            ReturnValue = Push(line.strip())
            if ReturnValue == -1:
                print("Stack full")
        file.close()
    except:
        print("File not found")

def calculate():
    global TopOfStack
    global Stack
    Value = Pop()
    Total = int(Value)
    while Value != "-1":
        Value = Pop()
        if Value == "+":
            Total += int(Pop())
        elif Value == "-":
            Total -= int(Pop())
        elif Value == "*":
            Total *= int(Pop())
        elif Value == "/":
            Total /= int(Pop())
    return Total

filename = input("Enter filename: ")
ReadData(filename)
print(calculate())