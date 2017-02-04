class SweetTomato:
    def __init__(self):
        self.cookedLevel = 0
        self.cookedString = "生的"
        self.zuoLiao = []

    def cook(self , i):
        self.cookedLevel += i
        strM = ''
        if self.cookedLevel > 8:
            strM = "烤糊了"
        elif self.cookedLevel > 5:
            strM = "熟了"
        elif self.cookedLevel > 3:
            strM = "半生不熟"
        else:
            strM = "生的"
        self.cookedString = strM

    def __str__(self):
        msg = self.cookedString
        msg += " 熟的程度为:" + str(self.cookedLevel) + " "
        if len(self.zuoLiao) > 0 :
            msg += "佐料为："
            msg += ','.join(self.zuoLiao)
        return msg

    def joinM(self, m):
        self.zuoLiao.append(m)

digua = SweetTomato()
digua.cook(6)
digua.joinM("辣椒酱")
digua.joinM("朝天椒")

print(digua)

digua2 = SweetTomato()
digua2.cook(10)
print(digua2)
