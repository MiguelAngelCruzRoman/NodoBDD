from faker import Faker
import mysql.connector
import random

# Conexión a la base de datos MySQL
db = mysql.connector.connect(
    host="localhost",
    user="MeteUnUser",
    password="TamborLaContra",
    database="nodoITST"
)

cursor = db.cursor()

# Instancia de Faker
fake = Faker('es_MX')


# Obtener EMPLEADO existentes
cursor.execute("SELECT ID_Empleado FROM EMPLEADO")
empleado_ids = [row[0] for row in cursor.fetchall()]

# Generar datos falsos y agregarlos a la tabla DOCENTE
for _ in range(30):  # Cambia 10 por el número de registros que desees crear
    id_empleado = random.choice(empleado_ids)
    tipo_contrato = random.choice([True, False])  # True para contrato fijo, False para contrato temporal
    area_conocimiento = fake.job()
    experiencia = fake.random_int(1, 30)

    # Insertar datos en la tabla DOCENTE
    cursor.execute("INSERT INTO DOCENTE (ID_Empleado,TipoContrato, AreaConocimiento, Experiencia) VALUES (%s,%s, %s, %s)",
                   (id_empleado,tipo_contrato, area_conocimiento, experiencia))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()
