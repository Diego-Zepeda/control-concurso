import json
import pickle
import random

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


def findProyectosJuez(juez):
    proyectos = cargar_proyectos()
    proyectosCalificados = []
    proyectosSinCalificar = []

    for proyecto in proyectos:
        calificaciones = proyecto["calificaciones"]
        calificado = False
        for calificacion in calificaciones:
            if calificacion["usuarioJuez"] == juez:
                calificado = True
                break
        if calificado:
            proyectosCalificados.append(proyecto)
        else:
            proyectosSinCalificar.append(proyecto)

    # Si tenemos proyectos sin calificar, ordena la lista de acuerdo al numero de calificaciones que tiene,
    # asi los proyectos que tienen 0 calificaciones, se califican primero y los que tienen muchas, al final.
    if len(proyectosSinCalificar) > 0:
        proyectosSinCalificar = sorted(proyectosSinCalificar, key=lambda i: i['calificacionesCount'])

    return dict(calificados=proyectosCalificados, noCalificados=proyectosSinCalificar)

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
    nombreData = json.loads(requests.get(f"https://uinames.com/api/?amount={num}").content.decode())
    for x in range(num):
        usuario = nombreData[x]["name"] + str(random.randrange(1000))
        nombre = nombreData[x]["name"] + " " + nombreData[x]["surname"]
        link = "raandsadasd.com"
        nivel = random.randint(1, 3)
        categoria = random.randint(1, 2)
        nuevoProyecto = dict(codigo=getNumeroProyecto(), usuario=usuario, nombre=nombre, link=link, nivel=nivel,
                             categoria=categoria, ganadorConsolaPC=False, ganadorMovil=False, ganadorGeneral=False,
                             calificacionesCount=0, calificaciones=list())

        agregarProyecto(nuevoProyecto)
        for n in range(5):
            calificaciones = (random.randrange(11), random.randrange(11), random.randrange(11), random.randrange(11),
                              random.randrange(11), random.randrange(11), random.randrange(11), random.randrange(11),
                              random.randrange(11), random.randrange(11))
            calificarProyecto(usuario, "randomJuez", calificaciones)


def caseNivelProyecto(nCaso):
    casos = {
        1: "Principiante",
        2: "Intermedio",
        3: "Avanzado",
    }
    return casos.get(nCaso)


def caseCategoriaProyecto(nCaso):
    casos = {
        1: "App Movil",
        2: "Consola o PC",
    }
    return casos.get(nCaso)

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
    proyectoCalificado["calificacionesCount"] += 1
    for proyecto in proyectos:

        if proyecto["usuario"] == usuarioProyecto:
            proyecto = proyectoCalificado
            break

    guardar_proyectos(proyectos)
