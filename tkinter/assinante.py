import time
import paho.mqtt.client as mqtt


class Assinante:

    def __init__(self):
        self.temperatura_quarto = 0
        self.temperatura_sala = 15
        self.presenciometro = "false"
        self.luminaria_exterior = "false"
        self.estado_porta = "false"
        self.client = mqtt.Client()
        self.client.on_message = self.on_message

    def get_temperatura_sala(self):
        return self.temperatura_sala

    def get_temperatura_quarto(self):
        return self.temperatura_quarto

    def get_presenciometro(self):
        return self.presenciometro

    def get_luminaria_exterior(self):
        return self.luminaria_exterior

    def get_estado_porta(self):
        return self.estado_porta

    # Configura o nivel de qos.
    qos = 2

    def on_message(self, client, userdata, msg):
        print(f"Mensagem recebida no topico {msg.topic}: {msg.payload.decode()}")
        if msg.topic == "instrumentos/termometro/sala":
            self.temperatura_sala = msg.payload.decode()
        if msg.topic == "instrumentos/termometro/quarto":
            self.temperatura_quarto = msg.payload.decode()
        if msg.topic == "instrumentos/presenciometro/porta":
            self.presenciometro = msg.payload.decode()
        if msg.topic == "aparelhos/luminaria/exterior":
            self.luminaria_exterior = msg.payload.decode()
        if msg.topic == "aparelhos/fechadura/porta":
            self.estado_porta = msg.payload.decode()

    def conectar(self):
        # Conecta ao servidor.
        broker_address = "broker.emqx.io"
        broker_port = 1883
        print("Conectado ao broker!")
        self.client.connect(broker_address, broker_port)
        time.sleep(1)
        self.client.subscribe("instrumentos/#", self.qos)
        self.client.subscribe("aparelhos/#", self.qos)
        self.client.loop_forever()
