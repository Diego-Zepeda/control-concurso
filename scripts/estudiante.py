import os

from scripts.concurso import estadoConcurso, estadoRegistros, verMejoresCalificaciones
from scripts.proyectos import agregarProyecto, getNumeroProyecto
from scripts.usuarios import agregarUsuario
from scripts.utilidades import recibirOpcion


def panelEstudiante():
    nOpciones = 2
    os.system("cls")
    print("## Inicio como Estudiante ##")
    print("1 - Regresar al menu")
    print("2 - Iniciar sesión")
    if estadoRegistros():
        print("3 - Registrarse")
        nOpciones = 3
    _opPanel = recibirOpcion(input("\n¿Qué opción deseas? : "), nOpciones)

    return _opPanel


def registroEstudiante():
    rango = "estudiante"
    registroUsuario = agregarUsuario(rango)
    if registroUsuario is not None:
        print("El nuevo {} ha sido creado con exito.".format(rango))
        print("Ingrese los datos del nuevo proyecto: ")
        nombre = input("Nombre : ")
        link = input("Link de descarga : ")
        nivel = recibirOpcion(input("1-Principiante   2-Intermedio   3-Avanzado\n"
                                    "¿Qué categoría como desarrollador te consideras?: \n"), 3)
        categoria = recibirOpcion(input("1-App. Móvil   2-Consola o PC"
                                        "\n¿A que categoría pertenece su proyecto?\n"), 2)

        nuevoProyecto = dict(codigo=getNumeroProyecto(), usuario=registroUsuario, nombre=nombre, link=link, nivel=nivel,
                             categoria=categoria, ganadorConsolaPC=False, ganadorMovil=False, ganadorGeneral=False,
                             calificacionesCount=0, calificaciones=list())
        if (agregarProyecto(nuevoProyecto)):
            print("Felicidades. Su proyecto se ha registrado con exito.")
        else:
            print("Ha ocurrido un error al registrar su proyecto.")
        os.system("pause")
        panelEstudianteIniciado()


def panelEstudianteIniciado():
    while True:
        if estadoConcurso():
            os.system("cls")
            print("El concurso aún no finaliza, mantengase atento a su correo.")
            os.system("pause")
            break
        else:
            os.system("cls")
            print("El concurso se ha cerrado y los usuarios ganadores son los siguientes")
            verMejoresCalificaciones()
            os.system("pause")
            break
