class conta():
    def __init__(self,numero_conta:int,agencia:int) -> None:
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.saldo = 0

    def sacar(self,valor:int):
        self.saldo -= valor

    def depositar (self,valor:int):
        self.saldo += valor

    def __str__(self) -> str:
        return(f"Número da conta:{self.numero_conta}"
               f"Agencia:{self.agencia}"
               f"Número da conta:{self.numero_conta}"
               f"Saldo da conta:{self.saldo}"
               )    