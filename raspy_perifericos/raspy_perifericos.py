import time
import paho.mqtt.client as mqtt
import threading
from clp import CLP
from instrumento import Termometro


client = mqtt.Client()

# Configura o nivel de qos.
qos = 2

meuCLP = CLP("CLP_1")


def checarInstrumentos():
    while True:
        time.sleep(5)
        print("Checando instrumentos...")
        enviar_dados_instrumentais()


thread = threading.Thread(target=checarInstrumentos)
thread.start()


def enviar_dados_instrumentais():
    for instrumento in meuCLP.instrumentos:
        client.publish("instrumentos/" + instrumento.nome, instrumento.lerMedida(), qos)
    client.publish("aparelhos/luminaria/exterior", "ligar", qos)
    pass


def controle_luminaria(payload):
    if payload == "ligar":
        meuCLP.aparelhos[0].ligar()
    elif payload == "desligar":
        meuCLP.aparelhos[0].desligar()
    else:
        print("Comando desconhecido.")
    pass


# Lida com mensagens recebidas.
def on_message(client, userdata, msg):
    print(f"Mensagem recebida no topico {msg.topic}: {msg.payload.decode()}")
    if msg.topic == "aparelhos/luminaria/exterior":
        controle_luminaria(msg.payload.decode())


client.on_message = on_message

# Conecta ao servidor.
broker_address = "broker.emqx.io"
broker_port = 1883

client.connect(broker_address, broker_port)

# Da tempo para o cliente se conectar. o metodo client.is_connected() esta sempre retornando falso, mesmo se o cliente estiver conectado, nao tenho certeza de por que.
time.sleep(1)


client.subscribe("instrumentos/#", qos)
client.subscribe("aparelhos/#", qos)


# client.publish(topic, payload, qos)

# client.publish(topic, "abcasdsa", qos)

client.loop_forever()
