import os

from scripts.concurso import estadoConcurso, estadoRegistros, verMejoresCalificaciones
from scripts.proyectos import agregarProyecto, getNumeroProyecto
from scripts.usuarios import agregarUsuario
from scripts.utilidades import recibirOpcion


def panelEstudiante():
    nOpciones = 1
    os.system("cls")
    print("## Inicio como Estudiante ##")
    print("1 - Iniciar sesión")
    if estadoRegistros():
        print("2 - Registrarse")
        nOpciones = 2
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
                                        "¿A que categoría pertenece su proyecto?\n"), 2)

        calificaciones = [dict(usuarioJuez="",
                               originalidad=tuple(),
                               creatividad=tuple(),
                               innovacionImpacio=tuple(),
                               complejidadTecnica=tuple(),
                               capacidadComercializacion=tuple(),
                               experienciaJuego=tuple(),
                               diseno=tuple(),
                               arte=tuple(),
                               musica=tuple(),
                               estrategiaJuego=tuple()
                               )]
        nuevoProyecto = dict(codigo=getNumeroProyecto(), usuario=registroUsuario, nombre=nombre, link=link, nivel=nivel,
                             categoria=categoria, ganadorConsolaPC=False, ganadorMovil=False, ganadorGeneral=False,
                             calificacion=0, calificaciones=list())
        if (agregarProyecto(nuevoProyecto)):
            print("Felicidades. Su proyecto se ha registrado con exito.")
        else:
            print("Ha ocurrido un error al registrar su proyecto.")
        os.system("pause")
        panelEstudianteIniciado()


def panelEstudianteIniciado():
    while True:
        if estadoConcurso():
            print("El concurso aún no finaliza, mantengase atento a su correo.")
        else:
            print("El concurso se ha cerrado y los usuarios ganadores son los siguientes")
            verMejoresCalificaciones()
            break
        os.system("pause")
