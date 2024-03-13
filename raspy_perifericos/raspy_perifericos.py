import time
import paho.mqtt.client as mqtt
import threading
import clp

client = mqtt.Client()

# Configura o nivel de qos.
qos = 2

meuCLP = clp.CLP("CLP_1")


def checar_instrumentos():
    while True:
        time.sleep(5)
        print("Checando instrumentos...")
        publicar_dados_instrumentais()


thread = threading.Thread(target=checar_instrumentos)
thread.start()


def publicar_dados_instrumentais():
    for instrumento in meuCLP.instrumentos:
        client.publish(
            "instrumentos/" + instrumento.nome, instrumento.ler_medida(), qos
        )
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
        controle_luminaria(msg.payload.decode())qw!~a@T4F1


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
