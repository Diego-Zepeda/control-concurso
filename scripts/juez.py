import os
from time import sleep

from scripts.concurso import verMejoresCalificaciones, estadoConcurso
from scripts.proyectos import descalificarProyecto, findProyectosJuez, caseCategoriaProyecto, caseNivelProyecto, \
    calificarProyecto
from scripts.utilidades import recibirOpcion


def panelJuez(userJuez):
    while True:
        os.system("cls")
        print("## PANEL DE JUEZ ##")
        _opPanel = recibirOpcion(input(".- Proyectos -.\n"
                                       "1 - Calificar proyectos\n"
                                       "2 - Ver proyectos ya calificados\n"
                                       "3 - Ver proyectos sin calificar\n"
                                       "4 - Descalificar proyecto\n"
                                       "\n"
                                       "5 - Cerrar sesion"
                                       "\n¿Qué opción deseas? : "), 5)

        # Cerrar el concurso. #
        if _opPanel == 1:
            if estadoConcurso():
                proyectos = findProyectosJuez(userJuez)["noCalificados"]
                criterios = ["originalidad",
                             "Creatividad",
                             "Innovacion e impacio",
                             "Complejidad técnica",
                             "Capacidad comercializacion",
                             "Experiencia de juego",
                             "Diseño",
                             "Arte",
                             "Música y sonido",
                             "Estrategia de juego"]

                for proyecto in proyectos:
                    os.system("cls")
                    print(f"CALIFICAR PROYECTO")
                    verProyecto(proyecto)
                    calificaciones = []
                    print("Calificación de 1 a 10 en:")
                    for criterio in criterios:
                        cal = recibirOpcion(input(" - " + criterio + " : "), 10)
                        calificaciones.append(cal)
                    os.system("cls")
                    print("Guardando calificaciones ingresadas..")
                    calificarProyecto(proyecto["usuario"], userJuez, calificaciones)
                    sleep(3)
                    print("¿Desea seguir calificando proyectos?\n"
                          "1 - Sí       2 - No\n")
                    _opcion = recibirOpcion(input(), 2)

                    if _opcion == 2:
                        break

            else:
                print("Concurso ya cerrado. Ya no es posible calificar.")
                print("Los ganadores fueros:")
                verMejoresCalificaciones()
            os.system("pause")

        # Ver proyectos calificados.
        if _opPanel == 2:
            proyectos = findProyectosJuez(userJuez)["calificados"]
            print(f"--- {len(proyectos)} Proyectos calificados ---")
            for proyecto in proyectos:
                print("-----------------------------")
                verProyecto(proyecto)
            os.system("pause")

        # Ver proyectos sin calificar.
        if _opPanel == 3:
            proyectos = findProyectosJuez(userJuez)["noCalificados"]
            print(f"--- {len(proyectos)} Proyectos NO calificados ---")
            for proyecto in proyectos:
                print("-----------------------------")
                verProyecto(proyecto)
            os.system("pause")

        # Descalificar proyecto
        if _opPanel == 4:
            while True:
                os.system("cls")
                print("-- Descalificar proyecto --")
                nombreUsuario = input("Introduce el nombre del usuario del dueño del proyecto: ")
                if descalificarProyecto(nombreUsuario):
                    print(f"Proyecto '{nombreUsuario}' eliminado exitosamente.")
                    os.system("pause")
                    break
                else:
                    print(f"Proyecto de usuario '{nombreUsuario}' no existe.")
                    opcion = recibirOpcion(input("\n 1 - Reintentar con otro usuario."
                                                 "\n 2 - Salir"
                                                 "\n¿Qué opción desea? : "), 2)
                    if opcion == 2:
                        break

        # Salir. #
        if _opPanel == 5:
            break


def verProyecto(proyecto):
    print(f"Nombre : {proyecto['nombre']}\n"
          f"Usuario : {proyecto['usuario']}\n"
          f"Link al proyecto: {proyecto['link']}\n"
          f"Nivel: {caseNivelProyecto(proyecto['nivel'])}\n"
          f"Cateforia: {caseCategoriaProyecto(proyecto['categoria'])}\n")
