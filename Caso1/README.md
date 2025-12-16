# Proyecto: Generación de Datos Sintéticos para Scoring Crediticio

Este proyecto genera un conjunto de datos sintéticos en formato JSON y CSV para probar algoritmos de scoring crediticio en un sistema de préstamos personales.

## Requisitos

- Python 3.8 o superior
- Librerías:
  - `faker`

## Instalación

1. Clona este repositorio o descarga los archivos.
2. Asegúrate de tener Python instalado en tu sistema.
3. Instala las dependencias necesarias ejecutando:

   ```bash
   pip install faker
   ```

## Ejecución

1. Genera el archivo JSON con los datos sintéticos:

   ```bash
   python generar_clientes.py
   ```

   Esto creará un archivo llamado `clientes_sinteticos.json` en el directorio del proyecto.

2. Convierte el archivo JSON a CSV:

   ```bash
   python exportar_a_csv.py
   ```

   Esto generará un archivo llamado `clientes_sinteticos.csv` en el directorio del proyecto.

## Archivos Generados

- `clientes_sinteticos.json`: Contiene los datos sintéticos en formato JSON.
- `clientes_sinteticos.csv`: Contiene los datos sintéticos en formato CSV.

## Notas

- Asegúrate de que los archivos `.py` estén en el mismo directorio para que las rutas funcionen correctamente.
- Puedes modificar los scripts para ajustar los datos generados según tus necesidades.