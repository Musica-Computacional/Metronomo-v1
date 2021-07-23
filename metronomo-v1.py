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