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

# Obtener IDs de Administrativo existentes
cursor.execute("SELECT ID_Empleado FROM ADMINISTRATIVO")
administrativo_ids = [row[0] for row in cursor.fetchall()]

# Generar datos falsos y agregarlos a la tabla NORMATIVA
for _ in range(50):  # Cambia 10 por el número de registros que desees crear
    nombre = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
    descripcion = fake.text()
    accion = fake.text()
    sancion = fake.text()
    administrativo_aprovador = random.choice(administrativo_ids)

    # Insertar datos en la tabla NORMATIVA
    cursor.execute("INSERT INTO NORMATIVA (Nombre, Descripcion, Accion, Sancion, AdministrativoAprovador) VALUES (%s, %s, %s, %s, %s)",
                   (nombre, descripcion, accion, sancion, administrativo_aprovador))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()
