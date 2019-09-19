import pickle

from scripts.proyectos import cargar_proyectos
from scripts.utilidades import findDicInList


def estadoConcurso():
    concurso = dict(estadoConcurso=True, registrosHabilitados=True, ganadorGeneral=None, ganadorMovil=None,
                    ganadorConsolaPC=None)


def cerrarRegistros():
    concurso = cargar_estado_concurso()
    concurso["registrosHabilitados"] = False
    guardar_estado_concurso(concurso)


def cerrarConcurso():
    proyectos = cargar_proyectos()
    calificaciones = 0
    nCalificaciones = 0
    usuarioGanadorGeneral = ["", "", ""]
    usuarioGanadorConsolaPC = ["", "", ""]
    usuarioGanadorMovil = ["", "", ""]

    calificacionGanadorGeneral = [0, 0, 0]
    calificacionGanadorConsolaPC = [0, 0, 0]
    calificacionGanadorMovil = [0, 0, 0]

    for proyecto in proyectos:
        calificacionesJueces = proyecto["calificaciones"]
        nivel = proyecto["nivel"]
        categoria = proyecto["categoria"]
        usuario = proyecto["usuario"]
        for calificacionJuez in calificacionesJueces.items():
            calificaciones = nCalificaciones = promedioCalificaciones = 0

            for k, calificacion in calificacionJuez:
                calificaciones += calificacion
                nCalificaciones += 1

            promedioCalificaciones = calificaciones / nCalificaciones

            if promedioCalificaciones > calificacionGanadorGeneral[nivel]:
                calificacionGanadorGeneral[nivel] = promedioCalificaciones
                usuarioGanadorGeneral[nivel] = usuario
            if categoria == 1:
                if promedioCalificaciones > calificacionGanadorMovil[nivel]:
                    calificacionGanadorMovil[nivel] = promedioCalificaciones
                    usuarioGanadorMovil[nivel] = usuario
            else:
                if promedioCalificaciones > calificacionGanadorConsolaPC[nivel]:
                    calificacionGanadorConsolaPC[nivel] = promedioCalificaciones
                    calificacionGanadorConsolaPC[nivel] = usuario

    concurso = cargar_estado_concurso()
    concurso["registrosHabilitados"] = False
    guardar_estado_concurso(concurso)


def cargar_estado_concurso():
    try:
        with open("data/concurso.dat", "rb") as f:
            return pickle.load(f)
    except (OSError, IOError) as e:
        print(e)
        return list()


def guardar_estado_concurso(list):
    with open("data/concurso.dat", "wb") as f:
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
