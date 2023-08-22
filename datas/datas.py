class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano= ano
    
    def formatada(self):
        if self.mes < 10:
            return "{}/0{}/{}".format(self.dia, self.mes, self.ano)
        else:
            return "{}/{}/{}".format(self.dia, self.mes, self.ano)
