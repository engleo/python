class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano= ano
    
    def formatada(self):
        if self.mes < 10:
            print("{}/0{}/{}".format(self.dia, self.mes, self.ano))
        else:
            print("{}/{}/{}".format(self.dia, self.mes, self.ano))


d = Data(21,2,2023)
d.formatada()        