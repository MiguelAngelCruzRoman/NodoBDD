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

# Obtener ID de licenciatura existentes
cursor.execute("SELECT ID_Licenciatura FROM LICENCIATURA")
licenciatura_ids = [row[0] for row in cursor.fetchall()]

# Obtener número de control de alumno existentes
cursor.execute("SELECT NoControl FROM ALUMNO")
nocontrol_alumnos = [row[0] for row in cursor.fetchall()]

# Generar datos ficticios y agregarlos a la tabla ALUMNO_LICENCIATURA
for _ in range(100):  # Cambia 10 por el número de registros que desees crear
    id_licenciatura = random.choice(licenciatura_ids)
    nocontrol_alumno = random.choice(nocontrol_alumnos)

    # Insertar datos en la tabla ALUMNO_LICENCIATURA
    cursor.execute("INSERT INTO ALUMNO_LICENCIATURA (ID_Licenciatura, NoControl_Alumno) VALUES (%s, %s)",
                   (id_licenciatura, nocontrol_alumno))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()
