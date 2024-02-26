class Aparelho:
    estado = False  # Desligado

    def __init__(self, nome, codigo):
        self.nome = nome

    def ligar(self):
        raise Exception("Acao nao implementada!")

    def desligar(self):
        raise Exception("Acao nao implementada!")


class Ventilador(Aparelho):
    pass


class Luminaria(Aparelho):
    def __init__(self, nome, codigo):
        super().__init__(nome, codigo)

    def ligar(self):
        if self.estado == False:
            print("Ligando luminaria...")
            self.estado = True
        else:
            print("Luminaria ja se encontra ligada...")
        return self.estado

    def desligar(self):
        if self.estado == True:
            print("Desligando luminaria...")
            self.estado = False
        else:
            print("Luminaria ja se encontra desligada...")
        return self.estado


class Porta(Aparelho):
    pass
