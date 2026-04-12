def ReadData():
    strArray = []
    file = open("Data.txt", "r")
    for line in file:
        strArray.append(line.strip())
    file.close()
    return strArray

def FormatArray(array):
    output = array[0]
    for i in range(1, len(array)):
        output = output + " " + array[i]
    return output

def CompareStrings(string1, string2):
    for i in range(len(string1)):
        if string1[i] < string2[i]:
            return 1
        elif string1[i] > string2[i]:
            return 2

def Bubble(array):
    length = len(array)
    for i in range(length):
        swaps = False
        for j in range(length - 1):
            if CompareStrings(array[j], array[j+1]) == 2:
                array[j], array[j+1] = array[j+1], array[j]
                swaps = True
        if not swaps:
            break
    return array

array1 = ReadData()
array1 = Bubble(array1)
print(FormatArray(array1))
