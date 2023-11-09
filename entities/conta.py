from entities.historico import Historico


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print(f'\n{ " Operação falhou! Você não tem saldo suficiente. ".center(100, "@") }')

        elif valor > 0:
            self._saldo -= valor
            print(f'\n{ " Saque realizado com sucesso! ".center(100, "=") }')
            return True

        else:
            print(f'\n{ " Operação falhou! O valor informado é inválido. ".center(100, "@") }')

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f'\n{ " Depósito realizado com sucesso! ".center(100, "=") }')
        else:
            print(f'\n{ " Operação falhou! O valor informado é inválido. ".center(100, "@") }')
            return False

        return True
