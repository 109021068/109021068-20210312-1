class Hero:
    def __init__(self, name, gender, attack, denfense, blood, camp):
        self.studName = name
        self.studGender = gender
        self.studAttack = attack
        self.studDenfense = denfense
        self.studBlood = blood
        self.studCamp = camp
    def showInfo(self):
        print(self.studName)
        print(self.studGender)
        print(self.studAttack)
        print(self.studDenfense)
        print(self.studBlood)
        print(self.studCamp)
x = Hero("劉備","man","100000","1000000","100000","蜀")
x1 = Hero("關羽","man","1000000","100000","100000","蜀")
x2 = Hero("張飛","man","1000000","100000","100000","蜀")
x.showInfo()
x1.showInfo()
x2.showInfo()