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

average1, average2 = 0, 0
name1 = Horses[0].GetName()
name2 = Horses[1].GetName()
for i in range(4):
    fence = Course[i]
    success = Horses[0].Success(fence.GetHeight(), fence.GetRisk())
    print(f"The horse {name1} at fence {i+1} has a {success}")
    average1 += success
for i in range(4):
    fence = Course[i]
    success = Horses[1].Success(fence.GetHeight(), fence.GetRisk())
    print(f"The horse {name2} at fence {i+1} has a {success}")
    average2 += success
average1 /= 4
average2 /= 4

print(f"The horse {name1} has an average {average1}% chance of jumping over all four fences")
print(f"The horse {name2} has an average {average2}% chance of jumping over all four fences")

if average1 > average2:
    print(f"The horse with the highest chance of success is {name1}")
if average1 < average2:
    print(f"The horse with the highest chance of success is {name2}")
