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

# Obtener IDs de postgrado existentes
cursor.execute("SELECT ID_Postgrado FROM POSTGRADO")
postgrado_ids = [row[0] for row in cursor.fetchall()]

# Obtener números de control de alumno existentes
cursor.execute("SELECT NoControl FROM ALUMNO")
no_control_alumnos = [row[0] for row in cursor.fetchall()]

# Generar datos ficticios y agregarlos a la tabla ALUMNO_POSTGRADO
for _ in range(100):  # Cambia 10 por el número de registros que desees crear
    id_postgrado = random.choice(postgrado_ids)  # Seleccionar un ID de postgrado aleatorio
    no_control_alumno = random.choice(no_control_alumnos)  # Seleccionar un número de control de alumno aleatorio

    # Insertar datos en la tabla ALUMNO_POSTGRADO
    cursor.execute("INSERT INTO ALUMNO_POSTGRADO (ID_Postgrado, NoControl_Alumno) VALUES (%s, %s)",
                   (id_postgrado, no_control_alumno))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()
