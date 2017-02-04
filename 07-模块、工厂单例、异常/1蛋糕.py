class Caomei(object):
    def __init__(self):
        self.name = '草莓蛋糕'

class DangaoFactory(object):

    def makeDangao(self, name):
        if name == "caomei":
            return Caomei()

class Store(object):
    def __init__(self):
        self.factory = DangaoFactory()

    def makeOrder(self, name):
        self.dangao = self.factory.makeDangao(name)

store = Store()
store.makeOrder("caomei")

print(store.dangao.name)
