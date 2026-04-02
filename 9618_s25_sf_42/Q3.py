class Animal:
    def __init__(self, Name, Sound, Size, Intelligence):
        self.Name = Name #string
        self.Sound = Sound #string
        self.Size = Size #integer
        self.Intelligence = Intelligence #integer

    def Description(self):
        return f"The animal's name is {self.Name}, it makes a {self.Sound}, its size is {self.Size} and its intelligence is {self.Intelligence}"

class Parrot:
    def __init__(self, Name, Sound, Size, Intelligence, WingSpan, NumberWords):
        super().__init__(self)
        self.WingSpan = WingSpan #integer
        self.NumberWords = NumberWords #integer

    def ChangeNumberWords(self, NumberWords):
        self.NumberWords += NumberWords

    def Description(self):
        return f"The animal's name is {self.Name}, it makes a {self.Sound}, its size is {self.Size} and its intelligence is {self.Intelligence}. It has a wingspan of {self.WingSpan}cm and can say {self.NumberWords} words."
