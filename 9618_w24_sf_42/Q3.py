HighScores = []
for i in range(7):
    HighScores.append(["","",""])


def ReadData():
    try:
        File = open("HighScoreTable.txt", "r")
    except FileNotFoundError:
        print("File not found")
    linenumber = 0
    HighScores = []
    for line in File:
        index = linenumber // 3
        box = linenumber % 3
        if box == 0:
            HighScores.append(["","",""])
            HighScores[index][box] = line[:-1]
        else:
            HighScores[index][box] = int(line)
        linenumber += 1
    return HighScores


def OutputHighScores(HighScores):
    for Player in HighScores:
        print(f"{Player[0]} reached level {Player[1]} with a score of {Player[2]}")

def SortScores():
    global HighScores
    for i in range(len(HighScores)):
        swap = False
        for j in range(len(HighScores) - i - 1):
            if 100*HighScores[j][1] + HighScores[j][2] < 100*HighScores[j+1][1] + HighScores[j+1][2]:
                HighScores[j], HighScores[j+1] = HighScores[j+1], HighScores[j]
                swap = True
        if swap == False:
            break

HighScores = ReadData()
print("Before")
OutputHighScores(HighScores)
SortScores()
print("After")
OutputHighScores(HighScores)