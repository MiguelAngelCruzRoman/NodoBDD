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

# Obtener NoControl_Alumno existentes
cursor.execute("SELECT NoControl FROM ALUMNO")
nocontrol_alumnos = [row[0] for row in cursor.fetchall()]

# Generar datos falsos y agregarlos a la tabla SERVICIO_SOCIAL
for _ in range(50):  # Cambia por el número de registros que desees crear
    nocontrol_alumno = random.choice(nocontrol_alumnos)
    fecha_inicio = fake.date_between(start_date='-25y', end_date='today') #cambiar el rango del año
    fecha_fin = fake.date_between(start_date=fecha_inicio, end_date='today')
    horas_planeadas = fake.random_int(50, 500)
    horas_laboradas = fake.random_int(0, horas_planeadas)
    nombre_lugar = fake.company()
    area_aplicacion = fake.job()

    # Insertar datos en la tabla SERVICIO_SOCIAL
    cursor.execute("INSERT INTO SERVICIO_SOCIAL (NoControl_Alumno, FechaInicio, FechaFin, HorasPlaneadas, HorasLaboradas, NombreLugar, AreaAplicacion) VALUES (%s, %s, %s, %s, %s, %s, %s)", (nocontrol_alumno, fecha_inicio, fecha_fin, horas_planeadas, horas_laboradas, nombre_lugar, area_aplicacion))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()
