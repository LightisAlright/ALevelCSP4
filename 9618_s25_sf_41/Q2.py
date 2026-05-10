def ReadData():
    Lines = []
    FileName = input("Enter a file name: ")
    File = open(FileName, "r")
    for Line in File:
        Lines.append(Line)
    return Lines

def StoreData(DataToStore, FileName):
    try:
        File = open(FileName, "w")
    except:
        pass
    else:
        for Data in DataToStore:
            File.write(Data + "\n")

def SplitData(DataArray):
    Red = []
    Green = []
    Blue = []
    Orange = []
    Yellow = []
    Pink = []
    for i in range(len(DataArray)):
        Line = DataArray[i].split(",")
        Number = Line[0]
        Colour = Line[1].strip()
        if Colour == "red":
            Red.append(Number)
        elif Colour == "green":
            Green.append(Number)
        elif Colour == "blue":
            Blue.append(Number)
        elif Colour == "orange":
            Orange.append(Number)
        elif Colour == "yellow":
            Yellow.append(Number)
        elif Colour == "pink":
            Pink.append(Number)
    StoreData(Red, "Red.txt")
    StoreData(Green, "Green.txt")
    StoreData(Blue, "Blue.txt")
    StoreData(Orange, "Orange.txt")
    StoreData(Yellow, "Yellow.txt")
    StoreData(Pink, "Pink.txt")

Data = ReadData()
SplitData(Data)