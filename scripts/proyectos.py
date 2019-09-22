import json
import pickle
import random
import time

import requests

from scripts.utilidades import findDicInList


def agregarProyecto(nuevoProyecto):
    listProyectos = cargar_proyectos()
    listProyectos.append(nuevoProyecto)
    guardar_proyectos(listProyectos)
    return True


def getNumeroProyecto():
    proyectos = cargar_proyectos()
    return len(proyectos)

def cargar_proyectos():
    try:
        with open("data/proyectos.dat", "rb") as f:
            return pickle.load(f)
    except (OSError, IOError) as e:
        print(e)
        return list()


def guardar_proyectos(list):
    with open("data/proyectos.dat", "wb") as f:
        pickle.dump(list, f)


def descalificarProyecto(usuario):
    dicProyecto = findDicInList(cargar_proyectos(), usuario=usuario)
    listProyectos = cargar_proyectos()
    for dic in listProyectos:
        if dicProyecto == dic:
            listProyectos.remove(dic)
            guardar_proyectos(listProyectos)
            return True
    return False

def generarProyectos(num):
    for x in range(num):
        nombreData = json.loads(requests.get("https://uinames.com/api/?minlen=15").content.decode())
        usuario = nombreData["name"] + str(random.randrange(1000))
        nombre = nombreData["name"] + " " + nombreData["surname"]
        link = "raandsadasd.com"
        nivel = random.randrange(3)
        categoria = random.randrange(3)
        nuevoProyecto = dict(codigo=getNumeroProyecto(), usuario=usuario, nombre=nombre, link=link, nivel=nivel,
                             categoria=categoria, ganadorConsolaPC=False, ganadorMovil=False, ganadorGeneral=False,
                             calificacion=0, calificaciones=list())

        agregarProyecto(nuevoProyecto)
        for n in range(5):
            calificaciones = (random.randrange(11), random.randrange(11), random.randrange(11), random.randrange(11),
                              random.randrange(11), random.randrange(11), random.randrange(11), random.randrange(11),
                              random.randrange(11), random.randrange(11))
            calificarProyecto(usuario, "randomJuez", calificaciones)
        print("Proyecto nuevo generado...")
        time.sleep(11)


def calificarProyecto(usuarioProyecto, usuarioJuez, tuplaCalificaciones):
    cal = dict(usuarioJuez=usuarioJuez,
               originalidad=0,
               creatividad=0,
               innovacionImpacio=0,
               complejidadTecnica=0,
               capacidadComercializacion=0,
               experienciaJuego=0,
               diseno=0,
               arte=0,
               musica=0,
               estrategiaJuego=0
               )
    n = 0
    for k, v in cal.items():
        if not isinstance(v, str):
            cal[k] = tuplaCalificaciones[n]
            n += 1

    proyectos = cargar_proyectos()
    proyectoCalificado = findDicInList(proyectos, usuario=usuarioProyecto)
    proyectoCalificado["calificaciones"].append(cal)
    for proyecto in proyectos:

        if proyecto["usuario"] == usuarioProyecto:
            proyecto = proyectoCalificado
            break

    guardar_proyectos(proyectos)
