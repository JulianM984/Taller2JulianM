import json
import csv

# Leer el archivo JSON
with open("clientes_sinteticos.json", "r", encoding="utf-8") as f:
    clientes = json.load(f)

# Escribir en un archivo CSV
with open("clientes_sinteticos.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)

    # Escribir encabezados
    encabezados = clientes[0].keys()
    writer.writerow(encabezados)

    # Escribir datos
    for cliente in clientes:
        writer.writerow(cliente.values())

print("Archivo 'clientes_sinteticos.csv' generado con éxito.")