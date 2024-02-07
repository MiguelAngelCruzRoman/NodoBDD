from faker import Faker
import mysql.connector
import random

# Conexión a la base de datos MySQL
db = mysql.connector.connect(
    host="localhost",
    user="Usuario",
    password="Contraseña",
    database="nodoITST"
)

cursor = db.cursor()

# Instancia de Faker
fake = Faker('es_MX')

# Obtener IDs de Empleado existentes
cursor.execute("SELECT ID_Empleado FROM EMPLEADO")
empleado_ids = [row[0] for row in cursor.fetchall()]

# Generar datos ficticios y agregarlos a la tabla NOMINA
for _ in range(200):  # Cambia 10 por el número de registros que desees crear
    id_empleado = random.choice(empleado_ids)
    monto = round(random.uniform(1000, 5000), 2)  # Monto aleatorio entre 1000 y 5000
    periodo = fake.month_name() + " " + fake.year()  # Periodo aleatorio (mes y año)
    dias_trabajados = fake.random_int(1, 30)  # Días trabajados aleatorios
    faltas = fake.random_int(0, 5)  # Faltas aleatorias
    deducciones = fake.sentence()  # Deducciones aleatorias
    sueldo = round(random.uniform(5000, 10000), 2)  # Sueldo aleatorio entre 5000 y 10000
    tipo_pago = fake.random_element(elements=("Transferencia bancaria", "Cheque", "Efectivo"))  # Tipo de pago aleatorio

    # Insertar datos en la tabla NOMINA
    cursor.execute("INSERT INTO NOMINA (ID_Empleado, Monto, Periodo, DiasTrabajados, Faltas, Deducciones, Sueldo, TipoPago) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                   (id_empleado, monto, periodo, dias_trabajados, faltas, deducciones, sueldo, tipo_pago))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()
