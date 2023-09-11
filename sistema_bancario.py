from abc import ABC, abstractmethod, abstractproperty
import datetime 
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        contas = []
        
    
    def realizar_transacao(self, conta, transacao):
        pass
    def adicionar_conta(self, conta):
        pass

class PessoaFisica(Cliente):
    def __init__(self,  cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Historico:
    def __init__(self) -> None:
        self._transacoes = []
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime('%d-%m-%Y %H:%M:%s'),
            }
        )

class Conta:
    def __init__(self, numero, cliente) -> None:
        self._saldo = 0
        self.numero = numero
        self.agencia = '0001'
        self.cliente = cliente
        self.historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    def sacar(self, valor):
        if valor > self._saldo:
            print("\n### Operação falhou! Você não tem saldo suficiente. ###")
        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True
        else:
            print("\n### Operação falhou! O valor informado é inválido. ###")
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
            return True
        else:
            print("\n### Operação falhou! O valor informado é inválido. ###")

        return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 500, limite_saques = 3) -> None:
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes 
             if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n### Operação falhou! O valor do saque excede o limite. ###")

        elif excedeu_saques:
            print("\n### Operação falhou! Número máximo de saques excedido. ###")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

    @property
    @abstractproperty
    def valor(self):
        pass

class Saque(Transacao):
    def __init__(self, valor) -> None:
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        transacao_ok = conta.sacar(self.valor)
        if transacao_ok:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor) -> None:
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        transacao_ok = conta.sacar(self.valor)
        if transacao_ok:
            conta.historico.adicionar_transacao(self)

