from instrumento import Termometro, Presenciometro


class CLP:
    instrumentos = [
        Termometro("termometro/sala", "28-031600c442ff"),
        # Termometro("Termometro_2", "codigo_aqui"),
        Presenciometro("presenciometro/porta", "codigo_aqui"),
    ]
    aparelhos = []

    def __init__(self, nome):
        self.nome = nome
