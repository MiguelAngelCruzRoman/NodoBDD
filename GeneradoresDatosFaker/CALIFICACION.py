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

# Obtener claves de curso existentes
cursor.execute("SELECT Clave FROM CURSO")
claves_curso = [row[0] for row in cursor.fetchall()]

# Obtener números de control de alumno existentes
cursor.execute("SELECT NoControl FROM ALUMNO")
nocontrol_alumnos = [row[0] for row in cursor.fetchall()]

# Obtener IDs de estatus existentes
cursor.execute("SELECT ID_Estatus FROM ESTATUS")
estatus_ids = [row[0] for row in cursor.fetchall()]

# Generar datos ficticios y agregarlos a la tabla CALIFICACION
for _ in range(100):  # Cambia 10 por el número de registros que desees crear
    acreditacion = fake.boolean()  # true es acreditado, false es no acreditado
    puntuacion = fake.random_int(min=0, max=100)  # Puntuación aleatoria
    clave_curso = random.choice(claves_curso)  # Clave de curso aleatoria
    nocontrol_alumno = random.choice(nocontrol_alumnos)  # Número de control de alumno aleatorio
    id_estatus = random.choice(estatus_ids)  # ID de estatus aleatorio

    # Insertar datos en la tabla CALIFICACION
    cursor.execute("INSERT INTO CALIFICACION (Acreditacion, Puntuacion, Clave_Curso, NoControl_Alumno, ID_Estatus_Estatus) VALUES (%s, %s, %s, %s, %s)",
                   (acreditacion, puntuacion, clave_curso, nocontrol_alumno, id_estatus))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()
