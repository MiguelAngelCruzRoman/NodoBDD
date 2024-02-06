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

# Obtener IDs de mobiliario existentes
cursor.execute("SELECT ID_Mobiliario FROM MOBILIARIO")
mobiliario_ids = [row[0] for row in cursor.fetchall()]

# Obtener IDs de aula existentes
cursor.execute("SELECT ID_Aula FROM AULA")
aula_ids = [row[0] for row in cursor.fetchall()]

# Generar datos ficticios y agregarlos a la tabla AULA_MOBILIARIO
for _ in range(200):  # Cambia 10 por el número de registros que desees crear
    id_mobiliario = random.choice(mobiliario_ids)  # Seleccionar un ID de mobiliario aleatorio
    id_aula = random.choice(aula_ids)  # Seleccionar un ID de aula aleatorio

    # Insertar datos en la tabla AULA_MOBILIARIO
    cursor.execute("INSERT INTO AULA_MOBILIARIO (ID_Mobiliario, ID_Aula) VALUES (%s, %s)",
                   (id_mobiliario, id_aula))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()
