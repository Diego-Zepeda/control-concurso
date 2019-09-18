import pickle
from time import sleep

from scripts.utilidades import findDicInList, recibirOpcion


def crearUsuarios():
    # Borra los datos existentes

    # Crea nuevos registros
    juez = dict(nombre="El juez pro", correo="juez@corre.com", usuario="juez", contrasena="pass", rango="juez")
    usuario = dict(usuario="estudiante", contrasena="pass", rango="estudiante")
    admin = dict(usuario="admin", contrasena="pass", rango="admin")

    listUsers = list()
    listUsers.append(juez)
    listUsers.append(usuario)
    listUsers.append(admin)

    guardar_usuarios(listUsers)


def agregarUsuario(rango):
    print("Ingrese los datos del nuevo {}.".format(rango))
    nombre = input("Nombre : ")
    usuario = input("Usuario : ")
    while True:
        if usuarioReutilizado(usuario):
            print("Nombre de usuario ya en uso, porfavor intente con otro.")
            sleep(2)
            usuario = input("Usuario : ")
        else:
            break
    contrasena = input("Contraseña : ")
    correo = input("Correo : ")
    if rango == "estudiante":
        telefonoCasa = input("Telefono de casa : ")
        numeroCelular = input("Numero celular :")
        ciudad = input("Ciudad : ")
        semestre = recibirOpcion(input("Semestre : "), 9)
        tituloCarrera = input("Titulo de carrera: ")
        uni = input("Universidad: ")
        nuevoUsuario = dict(nombre=nombre, usuario=usuario, contrasena=contrasena, correo=correo, rango=rango,
                            telefonoCasa=telefonoCasa,
                            numeroCelular=numeroCelular,
                            ciudad=ciudad,
                            semestre=semestre,
                            tituloCarrera=tituloCarrera,
                            universidad=uni)

    else:
        nuevoUsuario = dict(nombre=nombre, usuario=usuario, contrasena=contrasena, correo=correo, rango=rango)

    listUsuarios = cargar_usuarios()
    listUsuarios.append(nuevoUsuario)
    guardar_usuarios(listUsuarios)
    return usuario


def cargar_usuarios():
    try:
        with open("data/usuarios.dat", "rb") as f:
            return pickle.load(f)
    except (OSError, IOError) as e:
        print(e)
        return list()


def guardar_usuarios(list):
    with open("data/usuarios.dat", "wb") as f:
        pickle.dump(list, f)


def usuarioReutilizado(usuario):
    if findDicInList(cargar_usuarios(), usuario=usuario) is None:
        return False
    else:
        return True


def eliminarUsuario(usuario):
    dicUsuario = findDicInList(cargar_usuarios(), usuario=usuario)
    listUsuarios = cargar_usuarios()
    for dic in listUsuarios:
        if dicUsuario == dic:
            listUsuarios.remove(dic)
            guardar_usuarios(listUsuarios)
            return True
    return False
