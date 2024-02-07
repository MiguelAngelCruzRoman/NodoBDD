from faker import Faker
import mysql.connector

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

# Generar datos falsos y agregarlos a la tabla ESTATUS
for _ in range(10):  # Cambia 10 por el número de registros que desees crear
    tipo = fake.word()
    descripcion = fake.text()

    # Insertar datos en la tabla ESTATUS
    cursor.execute("INSERT INTO ESTATUS (Tipo, Descripcion) VALUES (%s, %s)", (tipo, descripcion))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()
