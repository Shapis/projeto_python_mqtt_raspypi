import threading
from prototipo_tkinter_v3 import Application
from assinante import Assinante

tkinter = Application()
assinante = Assinante()

thread_assinante = threading.Thread(target=assinante.conectar)
thread_assinante.start()


tkinter.gerar_frame()
