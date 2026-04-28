class EventItems:
    def __init__(self, EventName, Type, Difficulty):
        self.__EventName = EventName
        self.__Type = Type
        self.__Difficulty = Difficulty

    def GetName(self):
        return self.__EventName

    def GetDifficulty(self):
        return self.__Difficulty

    def GetEventType(self):
        return self.__Type

Group = [
    EventItems("Bridge", "jump", 3),
    EventItems("Water wade", "swim", 4),
    EventItems("100 mile run", "run", 5),
    EventItems("Gridlock", "drive", 2),
    EventItems("Wall on wall", "jump", 4)
]

class Character:
    def __init__(self, CharacterName, Jump, Swim, Run, Drive):
        self.__CharacterName = CharacterName
        self.__Jump = Jump
        self.__Swim = Swim
        self.__Run = Run
        self.__Drive = Drive

    def GetName(self):
        return self.__CharacterName

    def CalculateScore(self, EventType, Difficulty):
        Difference = 0
        PercentageChance = 0
        if EventType == "jump":
            Difference = Difficulty - self.__Jump
        elif EventType == "swim":
            Difference = Difficulty - self.__Swim
        elif EventType == "run":
            Difference = Difficulty - self.__Run
        elif EventType == "drive":
            Difference = Difficulty - self.__Drive
        if Difference < 1:
            PercentageChance = 100
        elif Difference == 1:
            PercentageChance = 80
        elif Difference == 2:
            PercentageChance = 60
        elif Difference == 3:
            PercentageChance = 40
        elif Difference == 4:
            PercentageChance = 20
        return PercentageChance

Character1 = Character("Tarz", 5, 3, 5, 1)
Character2 = Character("Geni", 2, 2, 3, 4)

Score1, Score2 = 0, 0
for Event in Group:
    EventType = Event.GetEventType()
    Difficulty = Event.GetDifficulty()
    Chance1 = Character1.CalculateScore(EventType, Difficulty)
    Chance2 = Character2.CalculateScore(EventType, Difficulty)
    if Chance1 > Chance2:
        print(f"{Character1.GetName()} won the {Event.GetName()} event!")
        Score1 += 1
    elif Chance1 < Chance2:
        print(f"{Character2.GetName()} won the {Event.GetName()} event!")
        Score2 += 1
    else:
        print(f"The {Event.GetName()} event is a draw.")
if Score1 > Score2:
    print(f"{Character1.GetName()} won the group with {Score1} points!")
elif Score1 < Score2:
    print(f"{Character2.GetName()} won the group with {Score2} points!")
else:
    print("The group is a draw.")