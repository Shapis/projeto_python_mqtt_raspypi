class Aparelho:
    def __init__(self, nome, codigo):
        self.nome = nome

    def executarAcao(self):
        raise Exception("Acao nao implementada!")


class Ventilador(Aparelho):
    pass


class Luminaria(Aparelho):
    pass


class Porta(Aparelho):
    pass
