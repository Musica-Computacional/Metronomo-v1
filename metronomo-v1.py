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

    def stop_counter(self):
        """Stop counter by setting self.start to False."""
        self.start = False

    def counter(self, spinbox):
        """Control counter display and audio with calculated time delay.
        Args:
            spinbox (tkinter.Spinbox): tkinter Spinbox widget to get beat.
        """
        if self.start:
            self.beat = int(spinbox.get()[0])

            self.time = int((60 / self.bpm - 0.1) * 1000)  # Math for delay

            self.count += 1
            self.var.set(self.count)

            if self.count == 1:
                Beep(880, 100)
            elif self.count >= self.beat:
                self.count = 0
                Beep(440, 100)
            else:
                Beep(440, 100)

            # Calls this method after a certain amount of time (self.time).
            self.root.after(self.time, lambda: self.counter(spinbox))

def main():
    """Call Metronomo class instance with tkinter root class settings.
        Inicializar un objeto de tipo metronomo """
    root = Tk()
    root.title("Metronomo")

    beats = "4/4"
    Metronomo(root, beats)

    root.mainloop()

if __name__ == "__main__":
    main()