######################################################
# Diego Sevilla
# 17238
######################################################
# metronomo-v1.py
######################################################
# Archivo para la construccion de un metronomo
######################################################


from tkinter import *
from winsound import Beep

class Metronomo:
    """Clase que representa un Metronomo"""

    def __init__(self, window_, beats):
        """Metodo constructor para inicializacion de variables y user_interface().
        Args:
            window_ (tkinter.Tk): Instancia principal de la clase tkinter.
            beats (list): Lista con los tempos para el metronomo.
        """

        self.bpm    = 0
        self.beat   = 0
        self.time   = 0
        self.count  = 0
        
        self.window_   = window_
        self.beats  = beats
        self.start  = False

        self.var = StringVar()
        self.var.set(self.count)

        self.user_interface()
    

    def contador(self, spinbox):
        """Controlador del contador en el UI y los beeps de audio con el retrazo.
        Args:
            spinbox (tkinter.Spinbox): tkinter Spinbox para los beats.
        """
        if self.start:
            self.beat = int(spinbox.get()[0])

            if self.beat == 6 :  # 6/8 
                self.time = int((60 / (self.bpm / .5) - 0.1) * 1000)
            elif self.beat == 9 :  # 9/8 
                self.time = int((60 / (self.bpm / .4) - 0.1) * 1000)
            else:
                self.time = int((60 / self.bpm - 0.1) * 1000)  # el retrazo

            self.count += 1
            self.var.set(self.count)

            if self.count == 1:
                Beep(880, 100)
            elif self.count >= self.beat:
                self.count = 0
                Beep(440, 100)
            else:
                Beep(440, 100)

            # Se llama el metodo cada cierto periodo de timpo
            self.window_.after(self.time, lambda: self.contador(spinbox))


    def detener_contador(self):
        """Detener contador"""
        self.start = False

    def iniciar_contador(self, entry, spinbox):
        """Comienza contador si self.start es False.
        """
        if not self.start:
            try:
                self.bpm = int(entry.get())
            except ValueError:
                self.bpm = 70
            else:
                if self.bpm > 300:  # Limite para los beats por minuto bpm
                    self.bpm = 300

            self.start = True
            self.contador(spinbox)

    def user_interface(self):
        """Intefaz de usuario para el metronomo."""
        frame = Frame()
        frame.pack()

        entry = Entry(frame, width=12, justify="center",background="#82827e",foreground="white",)
        entry.insert(0, "70")
        entry.grid(row=0, column=0, padx=5, sticky="E")

        spinbox = Spinbox(frame, width=10, values=self.beats, wrap=True,background="#82827e",foreground="white",)
        spinbox.grid(row=0, column=1, sticky="E")

        bpmLabel = Label(frame, text="bpm:")
        bpmLabel.grid(row=0, column=0, sticky="W")

        timeLabel = Label(frame, text="Tempo:")
        timeLabel.grid(row=0, column=1, padx=5, sticky="W")

        countLabel = Label(frame, textvariable=self.var, font=("Arial", 40))
        countLabel.grid(row=1, column=0, columnspan=2)

        startButton = Button(frame, text="Play", width=16, height=2, background="#4a4a46", foreground="white",
                              command=lambda: self.iniciar_contador(entry,
                                                                 spinbox))
        startButton.grid(row=2, column=0, padx=10, sticky="W")

        stopButton = Button(frame, text="Stop", width=16, height=2, background="#4a4a46", foreground="white",
                             command=lambda: self.detener_contador())
        stopButton.grid(row=2, column=1, padx=10, sticky="E")


def main():
    """ Inicializar un objeto de tipo metronomo """
    window_ = Tk()
    window_.title("Metronomo")
    #window_.geometry("600x400")
    window_.configure(background='black')


    beats = ["2/4", "3/4","4/4","5/4","7/4","6/8","9/8"]
    Metronomo(window_, beats)

    window_.mainloop()

if __name__ == "__main__":
    main()