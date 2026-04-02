stack = []
for i in range(20):
    stack.append(-1)
TopOfStack = -1

def Push(thing):
    if TopOfStack == 19:
        return -1
    else:
        TopOfStack += 1
        stack[TopOfStack] = thing
        return 1

def Pop():
    if TopOfStack == -1:
        return "-1"
    else:
        thing = stack[TopOfStack]
        TopOfStack -= 1
        return thing

def ReadData(filename):
    global TopOfStack
    global stack
    try:
        file = open(filename)
        for line in file:
            returnvalue = Push(line.strip())
            if returnvalue == -1:
                print("Stack full")
        file.close()
    except:
        print("File not found")


def calculate():
    global TopOfStack
    global stack
    total = Pop()
    while 