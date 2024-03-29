from tkinter import *

# from assinante import Assinante

root = Tk()


class Application:
    def __init__(self, assinante):
        self.root = root
        self.assinante = assinante

    def gerar_frame(self):
        self.tela()
        self.frame_tela()
        root.mainloop()

    def tela(self):
        self.root.title("Interface")
        self.root.configure(bg="#808080")
        self.root.geometry("325x125")  # Diminuir a altura do root

    def frame_tela(self):
        self.frame = Frame(self.root, bd=2, relief=SOLID)
        self.frame.place(relx=0.015, rely=0, relwidth=0.97, relheight=0.97)
        self.textoscima()
        self.imagens()
        self.quadrado()

    def textoscima(self):
        self.msg2 = Label(self.root, text="Quarto")
        self.msg2.place(relx=0.479, rely=0.05)

        self.msg3 = Label(self.root, text="Sala")
        self.msg3.place(relx=0.657, rely=0.05)

        self.msg4 = Label(self.root, text="Status:")
        self.msg4.place(relx=0.815, rely=0.05)

        self.msg5 = Label(self.root, text="Status:")
        self.msg5.place(relx=0.12, rely=0.05)

        self.msg6 = Label(self.root, text="Status:")
        self.msg6.place(relx=0.12, rely=0.05)

        self.msg7 = Label(self.root, text="Status:")
        self.msg7.place(relx=0.31, rely=0.05)

        self.msgtest_lampada = Label(self.frame, text="Desligada")
        self.msgtest_lampada.place(relx=0.075, rely=0.22)

        self.msgtest_porta = Label(self.frame, text="Aberta")
        self.msgtest_porta.place(relx=0.83, rely=0.22)

        self.msgtest_presenca = Label(self.frame, text="Ausente")
        self.msgtest_presenca.place(relx=0.28, rely=0.22)
        self.refresh_textos()

    def refresh_textos(self):
        if self.assinante.get_presenciometro() == "true":
            self.msgtest_presenca.destroy()
            self.msgtest_presenca = Label(self.frame, text="Presente")
        elif self.assinante.get_presenciometro() == "false":
            self.msgtest_presenca.destroy()
            self.msgtest_presenca = Label(self.frame, text="Ausente")
        self.msgtest_presenca.place(relx=0.28, rely=0.22)

        if self.assinante.get_luminaria_exterior() == "true":
            self.msgtest_lampada.destroy()
            self.msgtest_lampada = Label(self.frame, text="Ligado")
        elif self.assinante.get_luminaria_exterior() == "false":
            self.msgtest_lampada.destroy()
            self.msgtest_lampada = Label(self.frame, text="Desligado")
        self.msgtest_lampada.place(relx=0.075, rely=0.22)

        if self.assinante.get_estado_porta() == "true":
            self.msgtest_porta.destroy()
            self.msgtest_porta = Label(self.frame, text="Aberta")
        elif self.assinante.get_estado_porta() == "false":
            self.msgtest_porta.destroy()
            self.msgtest_porta = Label(self.frame, text="Fechado")
        self.msgtest_porta.place(relx=0.83, rely=0.22)
        self.root.after(1000, self.refresh_textos)

    def imagens(self):
        clamp = "foto2.png"
        self.lampd = PhotoImage(file=clamp)
        self.motraima = Label(self.root, image=self.lampd)
        self.motraima.place(relwidth=0.1, relheight=0.39, relx=0.13, rely=0.53)

        cpeson = "foto3.png"
        self.peson = PhotoImage(file=cpeson)
        self.motraipeson = Label(self.root, image=self.peson)
        self.motraipeson.place(relwidth=0.15, relheight=0.39, relx=0.3, rely=0.53)

        ctemp = "foto4.png"
        self.temp = PhotoImage(file=ctemp)
        self.motraitemp = Label(self.root, image=self.temp)
        self.motraitemp.place(relwidth=0.1, relheight=0.4, relx=0.5, rely=0.53)

        self.temp2 = PhotoImage(file=ctemp)
        self.motraitemp2 = Label(self.root, image=self.temp2)
        self.motraitemp2.place(relwidth=0.1, relheight=0.4, relx=0.65, rely=0.53)

        cporta = "foto5.png"
        self.porta = PhotoImage(file=cporta)
        self.motraiporta = Label(self.root, image=self.porta)
        self.motraiporta.place(relwidth=0.1, relheight=0.4, relx=0.82, rely=0.53)

    def quadrado(self):
        x1, y1 = 10, 10
        x2, y2 = 50, 30
        centrox = (x1 + x2) // 2
        centroy = (y1 + y2) // 2

        self.canvas = Canvas(self.frame, width=50, height=50)
        self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", width=2)
        self.canvas.create_text(
            centrox,
            centroy,
            text="x",
            fill="black",
            font=("Arial", 9, "bold"),
            tags="temp_quarto",
        )
        self.canvas.place(relx=0.448, rely=0.15)
        x3, y3 = 10, 10
        x4, y4 = 50, 30
        centrox3 = (x3 + x4) // 2
        centroy3 = (y3 + y4) // 2

        self.canvas = Canvas(self.frame, width=50, height=50)
        self.canvas.create_rectangle(x3, y3, x4, y4, outline="black", width=2)
        self.canvas.create_text(
            centrox3,
            centroy3,
            text="z",
            fill="black",
            font=("Arial", 9, "bold"),
            tags="temp_sala",
        )
        self.canvas.place(relx=0.62, rely=0.15)
        self.refresh_quadrados()

    def update_temperature(self, temperatura_sala, temperatura_quarto):
        x1, y1 = 10, 10
        x2, y2 = 50, 30
        centrox = (x1 + x2) // 2
        centroy = (y1 + y2) // 2

        self.canvas = Canvas(self.frame, width=50, height=50)
        self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", width=2)
        self.canvas.delete("temp_quarto")
        self.canvas.create_text(
            centrox,
            centroy,
            text=str(temperatura_quarto),
            fill="black",
            font=("Arial", 9, "bold"),
            tags="temp_quarto",
        )
        self.canvas.place(relx=0.448, rely=0.15)
        x3, y3 = 10, 10
        x4, y4 = 50, 30
        centrox3 = (x3 + x4) // 2
        centroy3 = (y3 + y4) // 2

        self.canvas = Canvas(self.frame, width=50, height=50)
        self.canvas.create_rectangle(x3, y3, x4, y4, outline="black", width=2)
        self.canvas.delete("temp_sala")
        self.canvas.create_text(
            centrox3,
            centroy3,
            text=str(temperatura_sala),
            fill="black",
            font=("Arial", 9, "bold"),
            tags="temp_sala",
        )
        self.canvas.place(relx=0.62, rely=0.15)

    def refresh_quadrados(self):
        self.update_temperature(
            self.assinante.get_temperatura_sala(),
            self.assinante.get_temperatura_quarto(),
        )
        self.root.after(1000, self.refresh_quadrados)
