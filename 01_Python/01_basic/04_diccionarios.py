def run():

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
    
    # 'Colombia' in poblacion_paises
    # >>> True
    
    # poblacion_paises.get('Chile', 0)
    # Busca a Chile y retorna el valor
    # Si no existe devuelve cero

    # poblacion_paises['Chile'] = 16_123_456
    # inseta nuevo clave-valor

    # del poblacion_paises['Chile']


if __name__ == '__main__':
    run()