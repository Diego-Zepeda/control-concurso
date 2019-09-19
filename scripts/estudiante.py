import os

from scripts.proyectos import agregarProyecto
from scripts.usuarios import agregarUsuario
from scripts.utilidades import recibirOpcion


def panelEstudiante():
    os.system("cls")
    print("## Inicio como Estudiante ##")
    _opPanel = recibirOpcion(input("  1 - Iniciar sesión\n"
                                   "  2 - Registrarse"
                                   "\n¿Qué opción deseas? : "), 2)
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

        calificaciones = [dict(originalidad=tuple(),
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
        nuevoProyecto = dict(usuario=registroUsuario, nombre=nombre, link=link, nivel=nivel,
                             categoria=categoria, calificaciones=list())
        if (agregarProyecto(nuevoProyecto)):
            print("Felicidades. Su proyecto se ha registrado con exito.")
        else:
            print("Ha ocurrido un error al registrar su proyecto.")
        os.system("pause")
        panelEstudianteIniciado()


def panelEstudianteIniciado():
    while True:
        print("En espera de respuesta. Aún no se califica.")
