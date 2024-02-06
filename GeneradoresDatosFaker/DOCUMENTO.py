from faker import Faker
import mysql.connector
import random
import io
import base64

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

# Generar datos falsos y agregarlos a la tabla DOCUMENTO
for _ in range(50):  # Cambia 10 por el número de registros que desees crear
    nombre = fake.file_name(extension="pdf")
    descripcion = fake.text()
    ejemplo_texto = fake.text()
    ejemplo_bytes = ejemplo_texto.encode('utf-8')
    ejemplo_blob = base64.b64encode(ejemplo_bytes)
    requisitos_adicionales = fake.text() if random.random() > 0.5 else None

    # Insertar datos en la tabla DOCUMENTO
    cursor.execute("INSERT INTO DOCUMENTO (Nombre, Descripcion, Ejemplo, RequisitosAdicionales) VALUES (%s, %s, %s, %s)",
                   (nombre, descripcion, ejemplo_blob, requisitos_adicionales))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()
