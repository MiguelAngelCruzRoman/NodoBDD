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

# Obtener CONVENIO existentes
cursor.execute("SELECT ID_Convenio FROM CONVENIO")
convenio_ids = [row[0] for row in cursor.fetchall()]

# Generar datos falsos y agregarlos a la tabla CERTIFICADO
for _ in range(50):  # Cambia 10 por el número de registros que desees crear
    nombre = fake.word()
    duracion = fake.random_int(1, 12)  # Duración en meses, ajusta según tus necesidades
    modalidad = fake.random_element(elements=("Presencial", "En línea", "Semipresencial"))
    id_convenio = random.choice(convenio_ids) if random.random() > 0.5 else None  # Ajusta el rango según tus necesidades

    # Insertar datos en la tabla CERTIFICADO
    cursor.execute("INSERT INTO CERTIFICADO (Nombre, Duracion, Modalidad, ID_Convenio) VALUES (%s, %s, %s, %s)",
                   (nombre, duracion, modalidad, id_convenio))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()
