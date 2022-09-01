class Espresso:
    def __init__(self):
        self.base = "Espresso"

    def view(self):
        print(self.topLayer, self.midLayer, self.base, sep=',')

class Cappuccino(Espresso):
    def __init__(self):
        super().__init__()
        self.midLayer = "Steamed Milk"
        self.topLayer = "Milk Foam"

cup = Cappuccino()
cup.view()