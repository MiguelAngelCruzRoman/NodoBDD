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

# Obtener NoControl_Alumno existentes
cursor.execute("SELECT NoControl FROM ALUMNO")
nocontrol_alumnos = [row[0] for row in cursor.fetchall()]

# Generar datos falsos y agregarlos a la tabla DIRECCION
for _ in range(100):  # Cambia 10 por el número de registros que desees crear
    nocontrol_alumno = random.choice(nocontrol_alumnos)
    cp = fake.random_int(10000, 99999)
    estado = fake.state()
    municipio = fake.city()
    colonia = fake.city_suffix()
    calle = fake.street_name()
    no_ext = fake.random_int(1, 999)
    no_int = str(fake.random_int(1, 999)) if random.random() > 0.5 else None

    # Insertar datos en la tabla DIRECCION
    cursor.execute("INSERT INTO DIRECCION (NoControl_Alumno, CP, Estado, Municipio, Colonia, Calle, NoExt, NoInt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (nocontrol_alumno, cp, estado, municipio, colonia, calle, no_ext, no_int))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()
