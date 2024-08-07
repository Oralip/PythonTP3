import sqlite3
import datetime
from tkinter import simpledialog


class Subject:
    def __init__(self):
        self.observador_init = [] 
        self.observador_close = [] 

    def registro_inicio(self, obj):
        self.observador_init.append(obj)
    
    def registro_close(self, obj):
        self.observador_close.append(obj)

    def notificacion_inicio(self):
        for observer in self.observador_init:
            observer.update()
    
    def notificacion_close(self):
        for observer in self.observador_close:
            observer.update()

class Observador():
    def actualizar(self):
        raise NotImplementedError("Actualizacion")
    

class ObservadorInicio(Observador):
    def __init__(self, obj):
        self.objservado = obj
        self.objservado.registro_inicio(self)
        self.user = simpledialog.askstring(title="Usuario",
                                  prompt="Indica tu nombre de USUARIO:")

    def update(self, *args):
        mensaje = (f"{datetime.datetime.now()}: el USUARIO: {self.user} ha iniciado la aplicacion")
        print(mensaje)
        loggerDB(mensaje)

class ObservadorClose(Observador):
    def __init__(self, obj):
        self.observado = obj
        self.observado.registro_close(self)
    
    def update(self, *args):
        mensaje = (f"{datetime.datetime.now()}: La apliacion se ha cerrado")
        loggerDB(mensaje)
        print(mensaje)



def loggerDB(mensaje):
    conn = sqlite3.connect("logging.db")
    cursor = conn.cursor()

    sql = """CREATE TABLE IF NOT EXISTS logging
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 log varchar(50) NOT NULL)"""
    cursor.execute(sql)
    sql="INSERT INTO logging (log) VALUES (?)"
    cursor.execute(sql, (mensaje,))
    conn.commit()
    conn.close()