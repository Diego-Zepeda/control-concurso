# -*- coding: utf-8 -*-
import os

from scripts.estudiante import panelEstudiante, registroEstudiante
from scripts.sesion import iniciarSesion
from scripts.utilidades import recibirOpcion

radio = 3


def main():
    os.system("cls")
    print("Bienvenido al concurso")
    print("1 - Soy Juez\n"
          "2 - Soy Estudiante\n"
          # "3 - Soy Administrador\n"
          )
    opMenu = recibirOpcion(input("¿Qué opción desea? : "), 3)

    if opMenu == 1:
        iniciarSesion("juez")
    if opMenu == 2:
        if panelEstudiante() == 1:
            iniciarSesion("estudiante")
        else:
            registroEstudiante()
    if opMenu == 3:
        iniciarSesion("admin")


if __name__ == '__main__':
    while True:
        main()
