def recibirOpcion(valor, alcance):
    try:
        opcion = int(valor)
        if opcion > 0 and opcion <= alcance:
            return opcion
        else:
            raise ValueError
    except():
        opcion = recibirOpcion(input("Sólo se permiten usar NÚMEROS del 1 al {}".format(alcance), alcance))
    return opcion


def findDicInList(listDic, **kwargs):
    for dic in listDic:
        for key, value in kwargs.items():
            if dic[key] == value:
                return dic
    return None


def findDicsInList(listDic, **kwargs):
    dicsEncontrados = list()
    for dic in listDic:
        for key, value in kwargs.items():
            if dic[key] == value:
                dicsEncontrados.append(dic)

    if len(dicsEncontrados) == 0:
        return None
    else:
        return dicsEncontrados
