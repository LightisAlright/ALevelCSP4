WordArray = []
NumberWords = -1

def ReadWords(Filename):
    global WordArray
    global NumberWords
    File = open(Filename, "r")
    for Line in File:
        WordArray.append(Line.strip())
        NumberWords += 1
    Play()

def Play():
    global WordArray
    global NumberWords
    print(WordArray[0])
    print(f"Number of answers: {NumberWords}")
    answer = ""
    WordArray[0] = None
    correct = 0
    while answer != "no":
        answer = input("Enter a word: ").lower()
        if answer in WordArray:
            WordArray[WordArray.index(answer)] = None
            correct += 1
            print(f"{answer} is an answer!")
        else:
            print(f"{answer} is not an answer!")
    print(f"{(correct/NumberWords):.2f}% of answers are entered!")
    print("Missing answers: ")
    for unanswered in WordArray:
        if type(unanswered) == str:
            print(unanswered)



Difficulty = input("Enter easy, medium, or hard: ")
if Difficulty == "easy":
    ReadWords("Easy.txt")
elif Difficulty == "medium":
    ReadWords("Medium.txt")
elif Difficulty == "hard":
    ReadWords("Hard.txt")
