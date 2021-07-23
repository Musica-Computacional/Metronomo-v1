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

    def __init__(self, root, beats):
        """Metodo constructor para inicializacion de variables y user_interface().
        Args:
            root (tkinter.Tk): Instancia principal de la clase tkinter.
            beats (list): Lista con los tempos para el metronomo.
        """
        self.root   = root
        self.beats  = beats

        self.start  = False
        self.bpm    = 0
        self.count  = 0
        self.beat   = 0
        self.time   = 0

        self.var = StringVar()
        self.var.set(self.count)

        self.user_interface()

    def user_interface(self):
        """Intefaz de usuario para el metronomo."""
        frame = Frame()
        frame.pack()

        entry = Entry(frame, width=12, justify="center")
        entry.insert(0, "70")
        entry.grid(row=0, column=0, padx=5, sticky="E")

        spinbox = Spinbox(frame, width=10, values=self.beats, wrap=True)
        spinbox.grid(row=0, column=1, sticky="E")

        label_bpm = Label(frame, text="bpm:")
        label_bpm.grid(row=0, column=0, sticky="W")

        label_time = Label(frame, text="Tempo:")
        label_time.grid(row=0, column=1, padx=5, sticky="W")

        label_count = Label(frame, textvariable=self.var, font=("Arial", 40))
        label_count.grid(row=1, column=0, columnspan=2)

        button_start = Button(frame, text="Play", width=16, height=2,
                              command=lambda: self.iniciar_contador(entry,
                                                                 spinbox))
        button_start.grid(row=2, column=0, padx=10, sticky="W")

        button_stop = Button(frame, text="Stop", width=16, height=2,
                             command=lambda: self.detener_contador())
        button_stop.grid(row=2, column=1, padx=10, sticky="E")

    def iniciar_contador(self, entry, spinbox):
        """Comienza contador si self.start es False.
        """
        if not self.start:
            try:
                self.bpm = int(entry.get())
            except ValueError:
                self.bpm = 70
            else:
                if self.bpm > 300:  # Limits BPM
                    self.bpm = 300

            self.start = True
            self.contador(spinbox)

    def detener_contador(self):
        """Detener contador"""
        self.start = False

    def contador(self, spinbox):
        """Controlador del contador en el UI y los beeps de audio con el retrazo.
        Args:
            spinbox (tkinter.Spinbox): tkinter Spinbox widget to get beat.
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
            self.root.after(self.time, lambda: self.contador(spinbox))

def main():
    """ Inicializar un objeto de tipo metronomo """
    root = Tk()
    root.title("Metronomo")

    beats = ["2/4", "3/4","4/4","5/4","7/4","6/8","9/8"]
    Metronomo(root, beats)

    root.mainloop()

if __name__ == "__main__":
    main()