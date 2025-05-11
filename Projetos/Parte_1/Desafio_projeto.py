from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, endereco,):
        self.endereco=endereco
        self.contas= []

class Transacao(ABC):
    @abstractmethod
    def registrar(self,conta):
        pass
       
class Pessoa_Fisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento,):
        super().__init__(endereco)
        self.cpf= cpf
        self.nome= nome
        self.data_nascimento= data_nascimento

class Conta:
    def __init__(self, saldo, numero, agencia, cliente):
        self.saldo= saldo
        self.numero= numero
        self.agencia= agencia
        self.cliente= cliente
        self.historico= Historico()

class Conta_Corrente(Conta):
    def __init__(self,saldo, numero, agencia, limite, limite_saques, cliente):
        super().__init__(saldo, numero, agencia, cliente)
        self.limite= limite
        self.limite_saques= limite_saques

class Historico:
    def __init__(self):
        self.transacoes= []
    
    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)
    

class Deposito(Transacao):
    def __init__(self,valor):
        self.valor= valor
    
    def registrar(self, conta):
        if self.valor >0:
            conta.saldo += self.valor
            conta.historico.adicionar_transacao(self)
            print(f"Saldo atual: R${conta.saldo:.2f}\n")
            return True
        else:
            print("Digite valores positivos\n")
            return False

class Saque(Transacao):
    def __init__(self, valor):
        self.valor= valor
    def registrar(self, conta):
        if (self.valor <= conta.saldo):
            conta.saldo -= self.valor
            conta.historico.adicionar_transacao(self)
            print(f"Saldo atual: R${conta.saldo:.2f}\n")
            return True
        else:
            print("Saldo Insuficiente\n")
            return False
    

