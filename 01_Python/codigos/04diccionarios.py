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
    # for pais in poblacion_paises.values():
    #     print(pais)
    # for pais in poblacion_paises.items():
    #     print(pais)
    #     print(type(pais)) #son tuplas
    for pais, poblacion in poblacion_paises.items():
        print(pais)
        print(type(pais))
        print(poblacion)
        print(type(poblacion))


if __name__ == '__main__':
    run()