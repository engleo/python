from unittest import main, TestCase
from conta import Conta
from cadastrar_conta import cadastrar_conta

def set_saldo(saldo):
    conta = cadastrar_conta(1, "teste_saldo", saldo, "teste_saldo")
    return conta.saldo

class TestSaldo(TestCase):
    def test_set_saldo_igual_saldo(self):
        resultado = set_saldo(500)
        esperado = 500

        self.assertEqual(resultado, esperado) 

if __name__ == "__main__":
    main()