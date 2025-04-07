# Nombres de ciudades y días
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 2

# Datos de temperaturas reales simuladas [ciudad][día][semana]
# Estructura: temperaturas[ciudad][día][semana]
temperaturas = [
    # Quito
    [
        [14, 13],  # Lunes
        [15, 14],  # Martes
        [16, 14],  # Miércoles
        [17, 15],  # Jueves
        [16, 14],  # Viernes
        [15, 13],  # Sábado
        [14, 12],  # Domingo
    ],
    # Guayaquil
    [
        [29, 30],  # Lunes
        [30, 31],  # Martes
        [31, 30],  # Miércoles
        [32, 31],  # Jueves
        [33, 30],  # Viernes
        [31, 29],  # Sábado
        [30, 28],  # Domingo
    ],
    # Cuenca
    [
        [18, 17],  # Lunes
        [19, 18],  # Martes
        [20, 18],  # Miércoles
        [21, 19],  # Jueves
        [20, 18],  # Viernes
        [19, 17],  # Sábado
        [18, 16],  # Domingo
    ]
]

# Calcular y mostrar los promedios
for i, ciudad in enumerate(ciudades):
    print(f"\n🌆 Promedios semanales de temperatura para {ciudad}:")
    for semana in range(semanas):
        suma = 0
        for dia in range(len(dias)):
            suma += temperaturas[i][dia][semana]
        promedio = suma / len(dias)
        print(f"  Semana {semana + 1}: {promedio:.2f}°C")
