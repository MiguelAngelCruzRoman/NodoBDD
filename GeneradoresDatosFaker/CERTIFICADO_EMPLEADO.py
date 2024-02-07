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

# Obtener IDs de Certificado existentes
cursor.execute("SELECT ID_Certificado FROM CERTIFICADO")
certificado_ids = [row[0] for row in cursor.fetchall()]

# Obtener IDs de Empleado existentes
cursor.execute("SELECT ID_Empleado FROM EMPLEADO")
empleado_ids = [row[0] for row in cursor.fetchall()]

# Obtener IDs de Estatus existentes
cursor.execute("SELECT ID_Estatus FROM ESTATUS")
estatus_ids = [row[0] for row in cursor.fetchall()]

# Generar datos ficticios y agregarlos a la tabla CERTIFICADO_EMPLEADO
for _ in range(100):  # Cambia 10 por el número de registros que desees crear
    fecha_inicio = fake.date_between(start_date='-20y', end_date='today')
    fecha_fin = fake.date_between(start_date=fecha_inicio, end_date='today')
    observaciones = fake.text() if random.random() > 0.5 else None
    id_certificado = random.choice(certificado_ids)
    id_empleado = random.choice(empleado_ids)
    id_estatus = random.choice(estatus_ids)

    # Insertar datos en la tabla CERTIFICADO_EMPLEADO
    cursor.execute("INSERT INTO CERTIFICADO_EMPLEADO (FechaInicio, FechaFin, Observaciones, ID_Certificado, ID_Empleado, ID_Estatus) VALUES (%s, %s, %s, %s, %s, %s)",
                   (fecha_inicio, fecha_fin, observaciones, id_certificado, id_empleado, id_estatus))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()
