import threading
from prototipo_tkinter_v3 import Application
from assinante import Assinante


assinante = Assinante()
tkinter = Application(assinante)

thread_assinante = threading.Thread(target=assinante.conectar)
thread_assinante.start()


tkinter.gerar_frame()
