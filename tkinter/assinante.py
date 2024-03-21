import time
import paho.mqtt.client as mqtt


class Assinante:

    client = mqtt.Client()

    # Configura o nivel de qos.
    qos = 2

    def on_message(client, userdata, msg):
        print(f"Mensagem recebida no topico {msg.topic}: {msg.payload.decode()}")
        if msg.topic == "aparelhos/luminaria/exterior":
            pass

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
