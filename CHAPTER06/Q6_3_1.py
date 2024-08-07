class Nigiri:
    category = "にぎり"
    top = "ねた"
    base = "しゃり"
    def show_attributes(self):
        print("top: {}, base: {}, category: {}".format(self.top, self.base, self.category))

class Katsuo(Nigiri):
    top = "かつお"
    topping = "生姜とねぎ"
    prise = 100

    def show_attributes(self):
        super().show_attributes()
        print("topping: {}".format(self.topping))

K1 = Katsuo()
K1.show_attributes()
