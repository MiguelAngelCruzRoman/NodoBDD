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

# Generar datos ficticios y agregarlos a la tabla CICLO
for _ in range(30):  # Cambia 10 por el número de registros que desees crear
    fecha_inicio = fake.date_between(start_date='-30y', end_date='today')
    fecha_fin = fake.date_between(start_date=fecha_inicio, end_date='+1y')
    director = random.choice(empleado_ids)
    id_ciclo = fecha_inicio.strftime("%m%Y") + "-" + fecha_fin.strftime("%m%Y")

    # Insertar datos en la tabla CICLO
    cursor.execute("INSERT INTO CICLO (ID_Ciclo, Director, FechaInicio, FechaFin) VALUES (%s, %s, %s, %s)",
                   (id_ciclo, director, fecha_inicio, fecha_fin))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()
