class Horse:
    def __init__(self, Name, MaxFenceHeight, PercentageSuccess):
        self.__Name = Name #string
        self.__MaxFenceHeight = MaxFenceHeight #integer
        self.__PercentageSuccess = PercentageSuccess #integer

    def GetName(self):
        return self.__Name

    def GetMaxFenceHeight(self):
        return self.__MaxFenceHeight

    def Success(self, Height, Risk):
        if Height > self.__MaxFenceHeight:
            return 0.2 * self.__PercentageSuccess
        else:
            if Risk == 1:
                return self.__PercentageSuccess
            elif Risk == 2:
                return self.__PercentageSuccess * 0.9
            elif Risk == 3:
                return self.__PercentageSuccess * 0.8
            elif Risk == 4:
                return self.__PercentageSuccess * 0.7
            elif Risk == 5:
                return self.__PercentageSuccess * 0.6


class Fence:
    def __init__(self, Height, Risk):
        self.__Height = Height #integer
        self.__Risk = Risk #integer

    def GetHeight(self):
        return self.__Height

    def GetRisk(self):
        return self.__Risk

Horses = [Horse('Beauty', 150, 72), Horse('Jet', 160, 65)]
print(Horses[0].GetName())
print(Horses[1].GetName())

Course = []
FenceCount = 0
while FenceCount < 4:
    try:
        height = int(input(f"Height of fence {FenceCount + 1}: "))
        risk = int(input(f"Risk of fence {FenceCount + 1}: "))
    except ValueError:
        continue
    Course.append(Fence(height, risk))
    FenceCount += 1

for fence in Course:
