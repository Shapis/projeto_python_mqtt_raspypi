class Aparelho:
    estado = False  # Desligado

    def __init__(self, nome, codigo):
        self.nome = nome

    def executarAcao(self):
        raise Exception("Acao nao implementada!")


class Ventilador(Aparelho):
    pass


class Luminaria(Aparelho):
    def __init__(self, nome, codigo):
        super().__init__(nome, codigo)

    def executarAcao(self):
        if self.estado == False:
            print("Ligando luminaria...")
            self.estado = True
        else:
            print("Desligando luminaria...")
            self.estado = False
        return self.estado


class Porta(Aparelho):
    pass
