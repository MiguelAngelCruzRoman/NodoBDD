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

# Obtener IDs de edificios existentes
cursor.execute("SELECT ID_Edificio FROM EDIFICIO")
edificios_ids = [row[0] for row in cursor.fetchall()]

# Generar datos ficticios y agregarlos a la tabla AULA
for _ in range(200):  # Cambia 10 por el número de registros que desees crear
    id_edificio = random.choice(edificios_ids)  # Seleccionar un ID de edificio aleatorio
    numero_salon = fake.random_int(min=100, max=300)  # Generar un número de salón aleatorio de tres dígitos
    capacidad = fake.random_int(min=10, max=100)  # Generar una capacidad aleatoria entre 10 y 100
    descripcion = fake.text(max_nb_chars=200)  # Generar una descripción aleatoria

    # Insertar datos en la tabla AULA
    cursor.execute("INSERT INTO AULA (ID_Edificio, NumeroSalon, Capacidad, Descripcion) VALUES (%s, %s, %s, %s)",
                   (id_edificio, numero_salon, capacidad, descripcion))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()
