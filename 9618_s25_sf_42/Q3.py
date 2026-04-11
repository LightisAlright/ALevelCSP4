class Animal:
    def __init__(self, Name, Sound, Size, Intelligence):
        self.Name = Name #string
        self.Sound = Sound #string
        self.Size = Size #integer
        self.Intelligence = Intelligence #integer

    def Description(self):
        return f"The animal's name is {self.Name}, it makes a {self.Sound}, its size is {self.Size} and its intelligence is {self.Intelligence}."

class Parrot(Animal):
    def __init__(self, Name, Sound, Size, Intelligence, WingSpan, NumberWords):
        super().__init__(Name, Sound, Size, Intelligence)
        self.WingSpan = WingSpan #integer
        self.NumberWords = NumberWords #integer

    def ChangeNumberWords(self, WordCount):
        self.NumberWords += WordCount

    def Description(self):
        return f"The animal's name is {self.Name}, it makes a {self.Sound}, its size is {self.Size} and its intelligence is {self.Intelligence}. It has a wingspan of {self.WingSpan}cm and can say {self.NumberWords} words."

class Wolf(Animal):
    def __init__(self, Name, Sound, Size, Intelligence, TerritorySize):
        super().__init__(Name, Sound, Size, Intelligence)
        self.TerritorySize = TerritorySize #integer

    def SetTerritorySize(self, Size):
        self.TerritorySize += Size

    def Description(self):
        return f"The animal's name is {self.Name}, it makes a {self.Sound}, its size is {self.Size} and its intelligence is {self.Intelligence}. Its territory is {self.TerritorySize} square miles."

Parrot1 = Parrot("Chewie", "Squawk", 1, 10, 30, 29)
Wolf1 = Wolf("Nighteyes", "Howl", 8, 7, 100)
Horse1 = Animal("Copper", "Neigh", 10, 6)

Wolf1.SetTerritorySize(-20)
Parrot1.ChangeNumberWords(2)
print(Parrot1.Description())
print(Wolf1.Description())
print(Horse1.Description())