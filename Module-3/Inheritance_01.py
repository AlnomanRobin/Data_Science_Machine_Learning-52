#single inheritance
class father:
    def skills(self):
        print("I can code in C++")

class son(father):
    pass

karim = son()
karim.skills()

#higherarchical inheritance
class mom:
    def cooking(self, name):
        print(f"{name} is cooking delicious biryani")

class Aysha(mom):
    pass

class Kamal(mom):
    pass

kamal = Kamal()
aysha = Aysha()

kamal.cooking("Kamal")
aysha.cooking("Aysha")
