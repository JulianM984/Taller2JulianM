import json
import random
from faker import Faker
from datetime import datetime, timedelta, date

# Configuración inicial
fake = Faker("es_CO")
Faker.seed(42)
random.seed(42)

# Constantes
NUM_CLIENTES = 1000
CIUDADES = ["Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena", "Bucaramanga", "Pereira", "Manizales", "Cúcuta"]
CIUDADES_PROB = [0.4, 0.2, 0.15, 0.1, 0.05, 0.05, 0.025, 0.015, 0.01]
TIPOS_EMPLEO = ["Empleado", "Independiente", "Pensionado"]
TIPOS_EMPLEO_PROB = [0.7, 0.2, 0.1]
HISTORIAL_CREDITICIO = ["Excelente", "Bueno", "Regular", "Malo"]
HISTORIAL_PROB = [0.2, 0.4, 0.3, 0.1]

# Funciones auxiliares
def generar_id(consecutivo):
    fecha_actual = datetime.now().strftime("%Y%m%d")
    return f"CLT-{fecha_actual}-{consecutivo:04d}"

def generar_cedula():
    return fake.unique.random_int(min=1000000000, max=1999999999)

def generar_email(nombre):
    dominio = fake.domain_name(levels=1)
    return f"{nombre.lower().replace(' ', '.')}@{dominio}"

def calcular_score(historial):
    if historial == "Excelente":
        return random.randint(750, 850)
    elif historial == "Bueno":
        return random.randint(650, 749)
    elif historial == "Regular":
        return random.randint(550, 649)
    else:
        return random.randint(300, 549)

def calcular_deuda(historial, ingreso):
    if historial == "Excelente":
        return random.uniform(0, 0.2) * ingreso
    elif historial == "Bueno":
        return random.uniform(0.2, 0.4) * ingreso
    elif historial == "Regular":
        return random.uniform(0.4, 0.6) * ingreso
    else:
        return random.uniform(0.6, 0.8) * ingreso

def generar_cliente(consecutivo):
    nombre = fake.name()
    fecha_nacimiento = fake.date_of_birth(minimum_age=24, maximum_age=64)
    edad = (date.today() - fecha_nacimiento).days // 365  # Convertir datetime.now() a date.today()
    ingreso = random.randint(1500000, 20000000)
    historial = random.choices(HISTORIAL_CREDITICIO, HISTORIAL_PROB)[0]
    deuda = calcular_deuda(historial, ingreso)
    saldo_ahorros = random.randint(0, 50000000)
    tipo_empleo = random.choices(TIPOS_EMPLEO, TIPOS_EMPLEO_PROB)[0]
    antiguedad_laboral = random.randint(0, min(30, edad - 18))

    return {
        "id": generar_id(consecutivo),
        "cedulaCiudadania": generar_cedula(),
        "nombreCompleto": nombre,
        "email": generar_email(nombre),
        "telefono": fake.phone_number(),
        "fechaNacimiento": fecha_nacimiento.strftime("%Y-%m-%d"),
        "ciudadResidencia": random.choices(CIUDADES, CIUDADES_PROB)[0],
        "ingresoMensual": ingreso,
        "tipoEmpleo": tipo_empleo,
        "antiguedadLaboral": antiguedad_laboral,
        "historialCrediticio": historial,
        "deudaActual": round(deuda, 2),
        "saldoCuentaAhorros": saldo_ahorros,
        "scoreCrediticio": calcular_score(historial),
    }

# Generar clientes
clientes = [generar_cliente(i + 1) for i in range(NUM_CLIENTES)]

# Guardar en archivo JSON
with open("clientes_sinteticos.json", "w", encoding="utf-8") as f:
    json.dump(clientes, f, ensure_ascii=False, indent=4)

print("Archivo 'clientes_sinteticos.json' generado con éxito.")