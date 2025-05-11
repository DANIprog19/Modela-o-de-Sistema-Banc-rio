from abc import ABC, abstractmethod
import random 

class Cliente:
    def __init__(self, endereco,):
        self.endereco=endereco
        self.conta= None

class Transacao(ABC):
    @abstractmethod
    def registrar(self,conta):
        pass
       
class Pessoa_Fisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf= cpf
        self.nome= nome
        self.data_nascimento= data_nascimento

class Conta:
    def __init__(self, saldo, numero, agencia, cliente):
        self.saldo= saldo
        self.numero= numero
        self.agencia = agencia
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
        if self.valor > 0:
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
    
def main():
    clientes= {}
    while(True):
        print('''
    =================== Menu======================
          0. Sair
          1. Cadastar pessoa Fisica
          2. Criar Conta Corrente
          3. Listar Contas de Clientes
          4. Historico de Movimentações
          5. Depositar
          6. Sacar
    ==============================================
    '''
    )
        escolha = input("Escolha uma opcao!\n")
        match escolha:
            case '0':
                print("Saindo...")
                return 
            case '1':
                print("=========Cadastro de Pessoa Fisica==========\n")
                cpf= input("Seu CPF: \n")
                if cpf in clientes:
                    print("CPF já cadastrado!\n")
                else:
                    nome= input("Seu nome: \n")
                    data_nascimento= input("Sua data de nascimento: \n")
                    endereco= input("Seu Endereço com logradouro: \n")
                    novo_Usuario= Pessoa_Fisica (endereco, cpf, nome, data_nascimento)
                    clientes[cpf]= novo_Usuario
                    print("Cadastro realizado com sucesso!\n")

            case '2': 
                print("======== Abertura de Conta Corrente =========\n")
                cpf= input("Digite o seu CPF: \n")
                if cpf in clientes:
                    cliente= clientes[cpf]
                    if cliente.conta:
                        print("Esse cliente já possui uma conta cadastrada! \n")
                    else:
                        saldo = 0
                        numero= "".join (str(random.randint(0, 9)) for _ in range(11))
                        agencia = "0001"
                        limite = 500
                        limite_saques = 3
                        Nova_contaCorrente= Conta_Corrente(saldo, numero, agencia, limite, limite_saques, cliente)
                        cliente.conta = Nova_contaCorrente
                        print("Conta criada com sucesso! \n")
                
                else:
                    print("CPF não cadastrado! \n")

            case '3':
                print("================ Listar Contas ================\n")
                for cpf, cliente in clientes.items():
                    print(f"Nome: {cliente.nome}\n ")
                    print(f"Data de Nacimento: {cliente.data_nascimento} \n")
                    print(f"Endereço: {cliente.endereco}\n")
                    if cliente.conta:
                        conta = cliente.conta
                        print(f"Agência: {conta.agencia} \n")
                        print(f"Numero da Conta: {conta.numero} \n")
                    else:
                        print("Sem contas a serem mostradas! \n")
            case '4':
                print("=============== Historico de Movimentações =============\n")
                cpf= input("Digite o seu cpf: \n")
                if cpf in clientes:
                    cliente= clientes[cpf]
                    if cliente.conta:
                        conta = cliente.conta
                        print(f"Agência: {conta.agencia} \n")
                        print(f"Numero da Conta: {conta.numero} \n")
                        if not conta.historico.transacoes:
                            print("Sem movimentações! \n")
                        else:
                            for transacao in conta.historico.transacoes:
                                print(f"Transações realizadas: {type(transacao).__name__}\n")
                                print(f"R${transacao.valor:.2f}\n")
                    else:
                        print("Não possui conta: \n")
                else:
                    print("CPF não encontrado! \n")    

            case '5': 
                print("================== Deposito ====================\n")
                cpf= input("Digite o seu cpf: \n")
                if cpf in clientes:
                    cliente= clientes[cpf]
                    if cliente.conta:
                        valor= float(input("Informe o valor que deseja depositar: \n"))
                        conta = cliente.conta
                        deposito = Deposito(valor)
                        deposito.registrar(conta)
                    else:
                        print("Cliente não possui contas! \n")
                else:
                    print("CPF não encontrado! \n")
            
            case '6': 
                print("==================== Saque ======================\n")
                cpf= input("Digite o seu cpf: \n")
                if cpf in clientes:
                    cliente= clientes[cpf]
                    if cliente.conta:
                        valor= float(input("Informe o valor que deseja sacar: \n"))
                        conta = cliente.conta
                        saque = Saque(valor)
                        saque.registrar(conta)
                    else:
                        print("Cliente não possui contas! \n")
                else:
                    print("CPF não encontrado! \n")
            case _:
                print("Opção Inválida! \n")

if __name__ == "__main__":
    main()