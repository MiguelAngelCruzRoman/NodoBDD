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

# Obtener IDs de ciclo existentes
cursor.execute("SELECT ID_Ciclo FROM CICLO")
ciclo_ids = [row[0] for row in cursor.fetchall()]

# Generar datos ficticios y agregarlos a la tabla PLATAFORMA
for _ in range(20):  # Cambia 10 por el número de registros que desees crear
    nombre = fake.company()  # Nombre aleatorio
    capacidad_usuarios = random.randint(100, 10000)  # Capacidad de usuarios aleatoria
    tipo = fake.word()  # Tipo aleatorio
    descripcion = fake.text()  # Descripción aleatoria
    url = fake.url()  # URL aleatoria
    id_ciclo = random.choice(ciclo_ids)  # Seleccionar un ID de ciclo aleatorio

    # Insertar datos en la tabla PLATAFORMA
    cursor.execute("INSERT INTO PLATAFORMA (Nombre, CapacidadUsuarios, Tipo, Descripcion, URL, ID_Ciclo) VALUES (%s, %s, %s, %s, %s, %s)",
                   (nombre, capacidad_usuarios, tipo, descripcion, url, id_ciclo))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()
