# Proyecto: Generación de Transacciones Sintéticas

Este proyecto genera 10,000 transacciones sintéticas para la tabla `transacciones` en PostgreSQL, siguiendo las reglas de negocio especificadas.

## Requisitos Previos

1. **PostgreSQL**: Asegúrate de tener PostgreSQL instalado y configurado.
2. **Tabla `transacciones`**: La tabla debe existir con la siguiente estructura:

```sql
CREATE TABLE transacciones (
    id_transaccion VARCHAR(20) PRIMARY KEY,
    fecha_hora TIMESTAMP NOT NULL,
    id_cuenta_origen VARCHAR(15) NOT NULL,
    id_cuenta_destino VARCHAR(15),
    tipo_transaccion VARCHAR(20) NOT NULL,
    monto DECIMAL(15,2) NOT NULL,
    estado VARCHAR(20) NOT NULL,
    canal VARCHAR(20) NOT NULL,
    descripcion TEXT
);
```

3. **Archivo SQL**: El archivo `generate_transactions.sql` debe estar disponible en el directorio del proyecto.

## Pasos de Configuración

1. **Clonar el Proyecto**
   - Descarga o clona este repositorio en tu máquina local.

2. **Configurar la Base de Datos**
   - Crea una base de datos en PostgreSQL si no tienes una:
     ```sql
     CREATE DATABASE banco;
     ```
   - Conéctate a la base de datos:
     ```bash
     psql -U usuario -d banco
     ```

3. **Crear la Tabla `transacciones`**
   - Ejecuta el script para crear la tabla:
     ```sql
     CREATE TABLE transacciones (
         id_transaccion VARCHAR(20) PRIMARY KEY,
         fecha_hora TIMESTAMP NOT NULL,
         id_cuenta_origen VARCHAR(15) NOT NULL,
         id_cuenta_destino VARCHAR(15),
         tipo_transaccion VARCHAR(20) NOT NULL,
         monto DECIMAL(15,2) NOT NULL,
         estado VARCHAR(20) NOT NULL,
         canal VARCHAR(20) NOT NULL,
         descripcion TEXT
     );
     ```

4. **Generar las Transacciones**
   - Ejecuta el script `generate_transactions.sql` en tu base de datos:
     ```bash
     psql -U usuario -d banco -f generate_transactions.sql
     ```

5. **Insertar Transacciones Masivas**
   - Si prefieres usar el archivo de INSERTs:
     ```bash
     psql -U usuario -d banco -f inserts_transacciones.txt
     ```

## Notas
- Asegúrate de ajustar los parámetros de conexión (usuario, base de datos) según tu configuración.
- Este proyecto está diseñado para pruebas de rendimiento y generación de reportes históricos.

## Contacto
Para dudas o soporte, contacta al equipo de desarrollo.