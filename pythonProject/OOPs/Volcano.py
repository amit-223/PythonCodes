class Volcano():
    def __init__(self, volcanoName, country, lastEruptionYear):
        self.volcanoName = volcanoName
        self.country = country
        self.lastEruptionYear = lastEruptionYear


class Eruption(Volcano):
    def __init__(self):
        super().__init__(volcanoName, country, lastEruptionYear)

        volcanoList = []
        volcanoList.append(volcanoName)
        volcanoList.append(country)
        volcanoList.append(lastEruptionYear)

    def findVolcanoByCountry(self, volcanoList, country):
        if volcanoList[1] == country:
            return volcanoList
        else:
            return None

    def getVolcanoCategorization(self, volcanoList, volcanoName):
        current = 2021
        if volcanoList[0] == volcanoName:
            if (current - lastEruptionYear) > 0 or (current - lastEruptionYear) < 25:
                return "High"
            elif (current - lastEruptionYear) >= 25 or (current - lastEruptionYear) < 50:
                return "Low"


volcanoName = "MountEra"
country = "Itlay"
lastEruptionYear = 2021
li = []
li.append(volcanoName)
li.append(country)
li.append(lastEruptionYear)
v = Volcano(volcanoName, country, lastEruptionYear)
e = Eruption

#
# def findVolcanoByCountry(self, volcanoList, country=""):
#     if volcanoList[1] == country:
#         return volcanoList
#     else:
#         return None
#
# def getVolcanoCategorization(self, volcanoList, volcanoName="", current=2021):
#     if volcanoList[0] == volcanoName:
#         if (current - volcanoList[4]) >= 1 and (current - volcanoList[4]) < 25:
#             return "High"
#         elif (current - volcanoList[4]) >= 25 and (current - volcanoList[4]) < 50:
#             return "low"
#         else:
#             return "Active"
