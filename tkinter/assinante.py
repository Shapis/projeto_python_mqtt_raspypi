import time
import paho.mqtt.client as mqtt


class Assinante:

    def __init__(self):
        self.temperatura_quarto = 0
        self.temperatura_sala = 15
        self.presenca_porta = "ausente"
        self.client = mqtt.Client()
        self.client.on_message = self.on_message

    def get_temperatura_sala(self):
        return self.temperatura_sala

    def get_temperatura_quarto(self):
        return self.temperatura_quarto

    def get_presenca_porta(self):
        return self.presenca_porta

    client = mqtt.Client()

    # Configura o nivel de qos.
    qos = 2

    def on_message(self, client, userdata, msg):
        print(f"Mensagem recebida no topico {msg.topic}: {msg.payload.decode()}")
        if msg.topic == "instrumentos/termometro/sala":
            self.temperatura_sala = msg.payload.decode()
        if msg.topic == "instrumentos/termometro/quarto":
            self.temperatura_quarto = msg.payload.decode()
        if msg.topic == "instrumentos/presenciometro/porta":
            self.presenca_porta = msg.payload.decode()
        if msg.topic == "aparelhos/luminaria/quarto":
            print("Luminaria do quarto")

    client.on_message = on_message

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
