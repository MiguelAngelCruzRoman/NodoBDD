from faker import Faker
import mysql.connector
import random
from datetime import datetime, timedelta

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

# Obtener IDs de Beca existentes
cursor.execute("SELECT ID_Beca FROM BECA")
beca_ids = [row[0] for row in cursor.fetchall()]

# Obtener NoControl_Alumno existentes
cursor.execute("SELECT NoControl FROM ALUMNO")
nocontrol_alumnos = [row[0] for row in cursor.fetchall()]

# Generar datos falsos y agregarlos a la tabla BECA_ALUMNO
for _ in range(100):  # Cambia 10 por el número de registros que desees crear
    id_beca = random.choice(beca_ids)
    nocontrol_alumno = random.choice(nocontrol_alumnos)
    fecha_inicio = fake.date_between(start_date='-20y', end_date='today') #Cambiar el rango de la fecha
    fecha_final = fake.date_between(start_date=fecha_inicio, end_date='+1y') if random.random() > 0.5 else None

    # Insertar datos en la tabla BECA_ALUMNO
    cursor.execute("INSERT INTO BECA_ALUMNO (ID_Beca, NoControl_Alumno, FechaInicio, FechaFinal) VALUES (%s, %s, %s, %s)",
                   (id_beca, nocontrol_alumno, fecha_inicio, fecha_final))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()
