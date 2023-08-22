from unittest import main, TestCase
from datas import Data



class Testformatada(TestCase):
    def test_formatada(self):
        d = Data(21,2,2023)
        resultado = d.formatada()
        esperado = "21/02/2023"
        
        self.assertTrue(resultado == esperado)
        
    
if __name__ == "__main__":
    main()        