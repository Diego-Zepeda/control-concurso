import pickle

from scripts.proyectos import cargar_proyectos


def cerrarRegistros():
    concurso = cargar_estado_concurso()
    concurso["registrosHabilitados"] = False
    guardar_estado_concurso(concurso)


def estadoRegistros():
    concurso = cargar_estado_concurso()
    return concurso["registrosHabilitados"]


def estadoConcurso():
    concurso = cargar_estado_concurso()
    return concurso["estadoConcurso"]

def _guardar_ganadores(resultados):
    resUsers = resultados["usuarios"]
    userGanGen = resUsers[0]
    userGanCon = resUsers[1]
    userGanMov = resUsers[2]

    concurso = cargar_estado_concurso()
    concurso["ganadorGeneral"] = userGanGen
    concurso["ganadorMovil"] = userGanMov
    concurso["ganadorConsolaPC"] = userGanCon
    guardar_estado_concurso(concurso)

def cerrarConcurso():
    print("Cerrando concurso..")
    cerrarRegistros()

    resultados = mejoresCalificaciones()
    _guardar_ganadores(resultados)
    verMejoresCalificaciones()

    print("Concurso cerrado.\n")


def verMejoresCalificaciones(resultados):
    resCal = resultados["calificaciones"]
    calGanGen = resCal[0]
    calGanCon = resCal[1]
    calGanMov = resCal[2]

    resUsers = resultados["usuarios"]
    userGanGen = resUsers[0]
    userGanCon = resUsers[1]
    userGanMov = resUsers[2]

    print("---- GENERAL ----\n"
          f"Principiante - {userGanGen[0]} - {calGanGen[0]} \n"
          f"Intermedio - {userGanGen[1]} - {calGanGen[1]} \n"
          f"Avanzado - {userGanGen[2]} - {calGanGen[2]} \n")
    print("-- Consola --\n"
          f"Principiante - {userGanCon[0]} - {calGanCon[0]} \n"
          f"Intermedio - {userGanCon[1]} - {calGanCon[1]} \n"
          f"Avanzado - {userGanCon[2]} - {calGanCon[2]} \n")
    print("-- Movil --\n"
          f"Principiante - {userGanMov[0]} - {calGanMov[0]} \n"
          f"Intermedio - {userGanMov[1]} - {calGanMov[1]} \n"
          f"Avanzado - {userGanMov[2]} - {calGanMov[2]} \n")


def mejoresCalificaciones():
    proyectos = cargar_proyectos()

    usuarioGanadorGeneral = ["", "", ""]
    usuarioGanadorConsolaPC = ["", "", ""]
    usuarioGanadorMovil = ["", "", ""]

    calificacionGanadorGeneral = [0, 0, 0]
    calificacionGanadorConsolaPC = [0, 0, 0]
    calificacionGanadorMovil = [0, 0, 0]

    for proyecto in proyectos:
        print(proyecto)
        calificacionesJueces = proyecto["calificaciones"]

        nivel = proyecto["nivel"]
        categoria = proyecto["categoria"]
        usuario = proyecto["usuario"]
        CalificacionesJueces = nCalificacionesJueces = promedioGeneralJueces = 0.0
        for calificacionJuez in calificacionesJueces:
            calificacionesJuez = nCalificacionJuez = promedioCalificacionJuez = 0.0

            for k, calificacion in calificacionJuez.items():
                if not isinstance(calificacion, str):
                    calificacionesJuez += calificacion
                    nCalificacionJuez += 1
            promedioCalificacionJuez = calificacionesJuez / nCalificacionJuez

            CalificacionesJueces += promedioCalificacionJuez
            nCalificacionesJueces += 1
        promedioGeneralProyecto = CalificacionesJueces / nCalificacionesJueces

        if promedioGeneralProyecto > calificacionGanadorGeneral[nivel]:
            calificacionGanadorGeneral[nivel] = promedioGeneralProyecto
            usuarioGanadorGeneral[nivel] = usuario
        if categoria == 1:
            if promedioGeneralProyecto > calificacionGanadorMovil[nivel]:
                calificacionGanadorMovil[nivel] = promedioGeneralProyecto
                usuarioGanadorMovil[nivel] = usuario
        else:
            if promedioGeneralProyecto > calificacionGanadorConsolaPC[nivel]:
                calificacionGanadorConsolaPC[nivel] = promedioGeneralProyecto
                usuarioGanadorConsolaPC[nivel] = usuario

    res = dict(usuarios=[usuarioGanadorGeneral, usuarioGanadorMovil, usuarioGanadorConsolaPC],
               calificaciones=[calificacionGanadorGeneral, calificacionGanadorMovil, calificacionGanadorConsolaPC])
    return res

def cargar_estado_concurso():
    try:
        with open("data/concurso.dat", "rb") as f:
            return pickle.load(f)
    except (OSError, IOError) as e:
        print(e)
        return list()


def guardar_estado_concurso(dict):
    with open("data/concurso.dat", "wb") as f:
        pickle.dump(dict, f)
