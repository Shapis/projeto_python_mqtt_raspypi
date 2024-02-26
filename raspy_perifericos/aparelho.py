class Aparelho:
    estado = False  # Desligado

    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo

    def ligar(self):
        if self.estado == False:
            print(f"Ligando {self.nome}...")
            self.estado = True
        else:
            print(f"{self.nome} ja se encontra ligada...")
        return self.estado

    def desligar(self):
        if self.estado == True:
            print(f"Desligando {self.nome}...")
            self.estado = False
        else:
            print(f"{self.nome} ja se encontra desligada...")
        return self.estado


class Ventilador(Aparelho):
    def __init__(self, nome, codigo):
        super().__init__(nome, codigo)

    pass


class Luminaria(Aparelho):
    def __init__(self, nome, codigo):
        super().__init__(nome, codigo)

    pass


class Porta(Aparelho):
    def __init__(self, nome, codigo):
        super().__init__(nome, codigo)

    pass
