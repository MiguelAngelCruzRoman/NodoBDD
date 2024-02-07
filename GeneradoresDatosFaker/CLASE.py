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

# Obtener IDs de aula existentes
cursor.execute("SELECT ID_Aula FROM AULA")
aula_ids = [row[0] for row in cursor.fetchall()]

# Obtener IDs de horario existentes
cursor.execute("SELECT ID_Horario FROM HORARIO")
horario_ids = [row[0] for row in cursor.fetchall()]

# Obtener claves de curso existentes
cursor.execute("SELECT Clave FROM CURSO")
curso_claves = [row[0] for row in cursor.fetchall()]

# Generar datos ficticios y agregarlos a la tabla CLASE
for _ in range(100):  # Cambia 10 por el número de registros que desees crear
    id_aula = random.choice(aula_ids)  # Seleccionar un ID de aula aleatorio
    id_horario = random.choice(horario_ids)  # Seleccionar un ID de horario aleatorio
    clave_curso = random.choice(curso_claves)  # Seleccionar una clave de curso aleatoria

    # Insertar datos en la tabla CLASE
    cursor.execute("INSERT INTO CLASE (ID_Aula, ID_Horario, Clave_Curso) VALUES (%s, %s, %s)",
                   (id_aula, id_horario, clave_curso))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()
