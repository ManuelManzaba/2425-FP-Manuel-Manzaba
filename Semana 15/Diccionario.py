# Creando un diccionario con información personal
informacion_personal = {
    "nombre": "Camila Pinargote",
    "edad": 28,
    "ciudad": "Loja",
    "profesion": "Ingeniera",
    "fecha_nacimiento": "25/05/1996",  # Fecha de nacimiento
    "estado_civil": "Soltera",          # Estado civil
    "correo": "camila.pinargote96@example.com"  # Correo personal
}

# Accediendo y modificando el valor de "ciudad"
informacion_personal["ciudad"] = "Ibarra"

# Agregando una nueva clave-valor para "profesion"
informacion_personal["profesion"] = "Abogada"

# Verificando la existencia de la clave "telefono"
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0982593195"

# Eliminando la clave "edad"
del informacion_personal["edad"]

# Imprimiendo el diccionario final
print(informacion_personal)
