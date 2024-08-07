import datetime


def log_event(function):
    def envolver(*args, **kwargs):
        resultado = function(*args, **kwargs)
        # muentro en pantalla los eventos
        if function.__name__ == 'alta':
            mensaje = (f"{datetime.datetime.now()}: Se ha realizado el {function.__name__} de un nuevo registro")
            print(mensaje)
        elif function.__name__ == 'consultar_lista_playlist':
            mensaje = (f"{datetime.datetime.now()}: Se ha realizado la consulta de una playlist")
            print(mensaje)
        elif function.__name__ == 'modificar':
            mensaje = (f"{datetime.datetime.now()}: Se ha modificado un registro de la base de datos")
            print(mensaje)
        elif function.__name__ == 'borrar_playlist':
            mensaje = (f"{datetime.datetime.now()}: Se ha eliminado una playlist de la base de datos")       
        else:
            mensaje = (f"{datetime.datetime.now()}: Se ha eliminado una cancion de la base de datos")
            print(mensaje)

        # genero un .txt para guardar el registro de logs
        archivo = open('logs.txt', 'a')
        archivo.write(mensaje + "\n")
        archivo.close()
        return resultado
    return envolver
