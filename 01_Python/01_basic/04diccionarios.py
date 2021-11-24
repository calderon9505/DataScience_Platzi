def run():
    mi_dicc = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    # print(mi_dicc)
    # print(mi_dicc['llave1'])

    poblacion_paises = {
        'Argentina': 44938_712,
        'Brasil': 210_147_125, #numeros mas legibles
        'Colombia': 50_372424
    }

    # for pais in poblacion_paises.keys():
    #     print(pais)
    # for poblacion in poblacion_paises.values():
    #     print(poblacion)
    # for item in poblacion_paises.items():
    #     print(item)
    #     print(type(item)) #son tuplas
    for pais, poblacion in poblacion_paises.items():
        print(pais, "\t", type(pais))
        print(poblacion, "\t", type(poblacion))


if __name__ == '__main__':
    run()