import pickle

from scripts.utilidades import findDicInList


def agregarProyecto(nuevoProyecto):
    listProyectos = cargar_proyectos()
    listProyectos.append(nuevoProyecto)
    guardar_proyectos(listProyectos)
    return True


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
