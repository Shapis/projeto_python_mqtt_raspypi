from DS18B20 import DS18B20


class Instrumento:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo

    def ler_medida(self):
        raise Exception("Leitor nao implementado!")


class Termometro(Instrumento):
    def __init__(self, nome, codigo):
        super().__init__(nome, codigo)
        self.sensor = DS18B20(codigo)

    def ler_medida(self):
        return self.sensor.read_temp()[0]


class Presenciometro(Instrumento):
    def ler_medida(self):
        return 10
