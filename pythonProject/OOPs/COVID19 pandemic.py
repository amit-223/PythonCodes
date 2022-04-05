class City:
    def __init__(self, city_id, state_name, city_name, covidbeds, avlblcovbeds, ventilbeds, avlblventilbeds):
        self.city_id = city_id
        self.state_name = state_name
        self.city_name = city_name
        self.covidbeds = covidbeds
        self.avlblcovbeds = avlblcovbeds
        self.ventilbeds = ventilbeds
        self.avlblventilbeds = avlblventilbeds


class CovBedsAnalysis:
    @classmethod
    def __init__(cls, l, analysis_name):
        pass

    @classmethod
    def get_StateWiseAvlblBedStats(cls):
        pass


n = int(input())
l = []
for i in range(n):
    city_id = int(input())
    state_name = input()
    city_name = input()
    covidbeds = int(input())
    avlblcovbeds = int(input())
    ventilbeds = int(input())
    avlblventilbeds = int(input())
    l.append(City(city_id, state_name, city_name, covidbeds, avlblcovbeds, ventilbeds, avlblventilbeds))
