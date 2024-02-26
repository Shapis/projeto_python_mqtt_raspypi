from instrumento import Termometro, Presenciometro
from aparelho import Luminaria, Ventilador, Porta


class CLP:
    instrumentos = [
        Termometro("termometro/sala", "28-031600c442ff"),
        # Termometro("termometro/quarto", "codigo_aqui"),
        Presenciometro("presenciometro/porta", "codigo_aqui"),
    ]
    aparelhos = [
        Luminaria("luminaria/exterior", "codigo_aqui"),
        Ventilador("ventilador/sala", "codigo_aqui"),
        Ventilador("ventilador/quarto", "codigo_aqui"),
        Porta("porta/sala", "codigo_aqui"),
    ]

    def __init__(self, nome):
        self.nome = nome
