import os
from time import sleep

from scripts.administrador import panelAdmin
from scripts.estudiante import panelEstudianteIniciado
from scripts.usuarios import cargar_usuarios
from scripts.utilidades import recibirOpcion, findDicInList


def iniciarSesion(rango):
    _user = _pass = None
    while True:
        os.system("cls")
        print("--- Iniciar sesión como {} ---".format(rango.upper()))

        # Si está reintentando iniciar sesión,
        # con esto sólo vuelve a escibir la contraseña
        if _user == None:
            _user = input("Usuario : ")
        else:
            print("Usuario : {}".format(_user))
        _pass = input("Contraseña : ")

        res, resText = verificarSesion(_user, _pass, rango)
        print(respuestasVerificar(res))

        if res == 0:
            sleep(5)
            _iniciarPanel(rango)
            break

        elif res == 1:
            _opcion = recibirOpcion(input("1-Volver a intentar.\n"
                                          "2-Salir\n"
                                          "¿Qué opción deseas? : "), 2)
            if _opcion == 2:
                break
            else:
                os.system("cls")
        elif res == 2:
            print("Contacte a su administrador.")
            sleep(5)
            break
        else:
            print("Redirigiendo a pantalla inicial.")
            sleep(5)
            break


def _iniciarPanel(rango):
    # if rango == 'juez':
    #    panelJuez()
    if rango == 'estudiante':
        panelEstudianteIniciado()
    elif rango == 'admin':
        panelAdmin()


def verificarSesion(usuario, contrasena, rango):
    usuariosList = cargar_usuarios()
    dicUser = findDicInList(usuariosList, usuario=usuario)
    userExist = dicUser != None
    if userExist:
        if rango != dicUser['rango']:
            return 3, respuestasVerificar(3)
        elif (dicUser['contrasena'] == contrasena):

            return 0, respuestasVerificar(0)
        else:
            return 1, respuestasVerificar(1)
    else:
        return 2, respuestasVerificar(2)


def respuestasVerificar(nCaso):
    casos = {
        0: "Ha iniciado sesión con éxito... Redireccionando al panel.",
        1: "### Contraseña erronea ###",
        2: "### Usuario inexistente ###",
        3: "### Rango distinto ###"
    }
    return casos.get(nCaso)
