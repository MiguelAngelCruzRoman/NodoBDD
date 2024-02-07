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

# Generar datos falsos y agregarlos a la tabla BECA
for _ in range(50):  # Cambia 10 por el número de registros que desees crear
    nombre = fake.name()
    tipo = fake.word()
    beneficios = fake.text()
    duracion = random.choice(['Semestral', 'Bimestral', 'Anual'])
    requisitos = fake.text()

    # Insertar datos en la tabla BECA
    cursor.execute("INSERT INTO BECA (Nombre, Tipo, Beneficios, Duracion, Requsitos) VALUES (%s, %s, %s, %s, %s)",
                   (nombre, tipo, beneficios, duracion, requisitos))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()
