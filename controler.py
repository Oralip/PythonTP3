from tkinter import Tk
import vista
from observador import ObservadorInicio, ObservadorClose




class Controlador:
    def __init__(self, root):
        self.root_controlador = root
        self.objeto_view = vista.SpotMusicApp(self.root_controlador)

        self.ob1 = ObservadorInicio(self.objeto_view.modelo)
        self.ob2 = ObservadorClose(self.objeto_view.modelo)
        self.objeto_view.modelo.notificacion_inicio()

    def close_app(self):
        self.objeto_view.modelo.notificacion_close()
        self.root_controlador.destroy()

if __name__ == "__main__":
        root = Tk()
        aplicacion = Controlador(root)
        root.protocol("WM_DELETE_WINDOW", aplicacion.close_app)
        root.mainloop()
