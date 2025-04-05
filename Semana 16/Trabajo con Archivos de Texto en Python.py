# Escritura de Archivo de Texto
# Usamos 'with open' para asegurarnos de que el archivo se cierre automáticamente después de escribir
with open("my_notes.txt", "w") as file:
    file.write("Día 1: Comencé a aprender Python. ¡Me gusta mucho hasta ahora!\n")
    file.write("Día 2: Aprendí sobre variables, tipos de datos y estructuras de control.\n")
    file.write("Día 3: Descubrí cómo funcionan los bucles for y while. Muy útil.\n")
    file.write("Día 4: Empecé a trabajar con listas y diccionarios. Puedo guardar muchos datos ahora.\n")
    file.write("Día 5: Estoy aprendiendo sobre funciones. Son muy prácticas para reutilizar código.\n")
    file.write("Día 6: Hoy aprendí a trabajar con archivos de texto. ¡Esto es lo que estoy haciendo ahora!\n")
    file.write("Día 7: Pienso practicar más con proyectos pequeños para reforzar mis conocimientos.\n")

# Lectura de Archivo de Texto
# Ahora vamos a leer el contenido del archivo línea por línea y mostrarlo en consola
print("Leyendo el contenido del archivo 'my_notes.txt':\n")
with open("my_notes.txt", "r") as file:
    line_number = 1
    for line in file:
        print(f"Línea {line_number}: {line.strip()}")
        line_number += 1

# Nota: el método .strip() elimina los saltos de línea extra cuando imprimimos
