class ContaGeral():

    def __init__(self, nome, numero, tipo):

        self.nome=nome
        self.numero=numero
        self.tipo=tipo
        self.saldo=500
        self.limite=0
        self.status=False

    def ativar_conta(self):
        if self.status==False:
            self.status=True
            print("Sua conta está ATIVADA.")

    def desativar_conta(self):
        if self.saldo >= 0:
            if self.status==True:
                self.status=False
                print("Operação realizada com sucesso.\n"
                      "Sua conta foi desativada.")
            else:
                print("Operação cancelada. \n"
                      "Sua conta está negativada. Não foi possível desativar.")

    def depositar(self,deposito):
        if self.status==True:
            self.saldo=self.saldo+deposito
            print(f"Operação realizada com sucesso.\n"
                  f"Este é seu saldo atualizado: {self.saldo}")
        else:
            print(f"Operação cancelada.\n"
                  f"Não foi possível depositar.")


    def sacar(self,saque):
        if self.status==True:

            if saque > self.saldo+self.limite:
                print("Operação cancelada.\n"
                      "Não foi possível sacar. Limite da conta excedido.")

            else:
                self.saldo = self.saldo - saque
                print(f"Operação realizada com sucesso.\n"
                      f"Este é seu saldo atualizado: {self.saldo}")
        else:
            print("Sua conta está desativada.\n"
                  "Não será possível finalizar a operação.")

    def verificar_saldo(self):
        if self.status==True:
            print(f"Seu saldo é de {self.saldo}")
        else:
            print("Não foi possível verificar seu saldo.\n"
                  "Sua conta está desativada.")


    def ativar_limite(self):
        if self.status==True:
            self.limite=1500
            print(f"Limite liberado: {self.limite}")
        else:
            print("Não foi possível liberar o limite.")





