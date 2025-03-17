def calcular_temperatura_promedio(temperaturas):
    """
    Calcula la temperatura promedio de varias ciudades durante un período de tiempo.

    Parámetros:
    temperaturas (dict): Un diccionario donde las claves son los nombres de las ciudades
                         y los valores son listas de temperaturas (en grados Celsius)
                         registradas durante varias semanas.

    Retorna:
    dict: Un diccionario con las ciudades como claves y sus temperaturas promedio como valores.
    """
    promedios = {}

    for ciudad, temps in temperaturas.items():
        if temps:  # Verifica que la lista de temperaturas no esté vacía
            promedio = sum(temps) / len(temps)  # Calcula el promedio
            promedios[ciudad] = promedio  # Almacena el promedio en el diccionario
        else:
            promedios[ciudad] = None  # Si no hay temperaturas, asigna None

    return promedios


# Ejemplo de uso
temperaturas_ciudades = {
    "Ciudad A": [20, 22, 21, 19],
    "Ciudad B": [25, 27, 26, 24],
    "Ciudad C": [15, 16, 14, 17]
}

promedios = calcular_temperatura_promedio(temperaturas_ciudades)
print(promedios)  # Salida esperada: {'Ciudad A': 20.5, 'Ciudad B': 25.5, 'Ciudad C': 15.5}
