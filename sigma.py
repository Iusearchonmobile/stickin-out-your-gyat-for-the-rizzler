class Final:
    pass

class Ohio:
    def Ohio(self):
        print("Ohio")
        return Final()

class Your_3:
    def your(self):
        print("your")
        return Ohio()

class Me:
    def me(self):
        print("me")
        return Your_3()

# Line 4: Freaking come here
class Give:
    def Give(self):
        print("Give")
        return Me()

class Here:
    def here(self):
        print("here")
        return Give()

class Come:
    def come(self):
        print("come")
        return Here()

class Freaking:
    def Freaking(self):
        print("Freaking")
        return Come()

class Sigma:
    def sigma(self):
        print("sigma")
        return Freaking()

class Your_2:
    def your(self):
        print("your")
        return Sigma()

class Be:
    def be(self):
        print("be")
        return Your_2()

class Wanna:
    def wanna(self):
        print("wanna")
        return Be()

class Just:
    def just(self):
        print("just")
        return Wanna()

class I_word:
    def I(self):
        print("I")
        return Just()

class Tax:
    def tax(self):
        print("tax")
        return I_word()

class Fanum:
    def Fanum(self):
        print("Fanum")
        return Tax()

class So_2:
    def so(self):
        print("so")
        return Fanum()

class Youre_2:
    def Youre(self):
        print("You're")
        return So_2()

class Skibidi:
    def skibidi(self):
        print("skibidi")
        return Youre_2()

class So_1:
    def so(self):
        print("so")
        return Skibidi()

class Youre_1:
    def Youre(self):
        print("You're")
        return So_1()

class Rizzler:
    def rizzler(self):
        print("rizzler")
        return Youre_1()

class The:
    def the(self):
        print("the")
        return Rizzler()

class For:
    def for_word(self):
        print("for")
        return The()

class Gyatt:
    def gyatt(self):
        print("gyatt")
        return For()

class Your_1:
    def your(self):
        print("your")
        return Gyatt()

class Out:
    def out(self):
        print("out")
        return Your_1()

class main:
    def Sticking(self):
        print("Sticking")
        return Out()

main().Sticking().out().your().gyatt().for_word().the().rizzler().Youre().so().skibidi().Youre().so().Fanum().tax().I().just().wanna().be().your().sigma().Freaking().come().here().Give().me().your().Ohio()
