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

# Obtener IDs de clase existentes
cursor.execute("SELECT ID_CLASE FROM CLASE")
clase_ids = [row[0] for row in cursor.fetchall()]

# Obtener ALUMNO existentes
cursor.execute("SELECT NoControl FROM ALUMNO")
noControl = [row[0] for row in cursor.fetchall()]

# Generar datos ficticios y agregarlos a la tabla ALUMNO_CLASE
for _ in range(200):  # Cambia 10 por el número de registros que desees crear
    id_clase = random.choice(clase_ids)  # Seleccionar un ID de clase aleatorio
    no_control_alumno = random.choice(noControl)  # Selecciona un número de control aleatorio

    # Insertar datos en la tabla ALUMNO_CLASE
    cursor.execute("INSERT INTO ALUMNO_CLASE (ID_CLASE, NoControl_Alumno) VALUES (%s, %s)",
                   (id_clase, no_control_alumno))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()
