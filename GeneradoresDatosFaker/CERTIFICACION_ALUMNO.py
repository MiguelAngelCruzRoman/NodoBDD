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

# Obtener números de control de Alumno existentes
cursor.execute("SELECT NoControl FROM ALUMNO")
nocontrol_alumnos = [row[0] for row in cursor.fetchall()]

# Obtener IDs de Estatus existentes
cursor.execute("SELECT ID_Estatus FROM ESTATUS")
estatus_ids = [row[0] for row in cursor.fetchall()]

# Generar datos falsos y agregarlos a la tabla CERTIFICACION_ALUMNO
for _ in range(100):  # Cambia 10 por el número de registros que desees crear
    fecha_inicio = fake.date_between(start_date='-20y', end_date='today')
    fecha_fin = fake.date_between(start_date=fecha_inicio, end_date='today')
    observaciones = fake.text() if random.random() > 0.5 else None
    id_certificado = random.choice(certificado_ids)
    nocontrol_alumno = random.choice(nocontrol_alumnos)
    id_estatus = random.choice(estatus_ids)

    # Insertar datos en la tabla CERTIFICACION_ALUMNO
    cursor.execute("INSERT INTO CERTIFICACION_ALUMNO (FechaInicio, FechaFin, Observaciones, ID_Certificado, NoControl_Alumno, ID_Estatus) VALUES (%s, %s, %s, %s, %s, %s)",
                   (fecha_inicio, fecha_fin, observaciones, id_certificado, nocontrol_alumno, id_estatus))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()
