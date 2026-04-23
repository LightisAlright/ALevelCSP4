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

    Get()