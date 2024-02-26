from instrumento import Termometro, Presenciometro


class CLP:
    instrumentos = [
        Termometro("Termometro_1", "28-031600c442ff"),
        # Termometro("Termometro_2", "codigo_aqui"),
        Presenciometro("Presenciometro_1", "codigo_aqui"),
    ]

    def __init__(self, nome):
        self.nome = nome
