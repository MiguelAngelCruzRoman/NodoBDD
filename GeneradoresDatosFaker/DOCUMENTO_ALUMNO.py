from faker import Faker
import mysql.connector
import random
import io
import base64

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

# Obtener IDs de Documento existentes
cursor.execute("SELECT ID_Documento FROM DOCUMENTO")
documento_ids = [row[0] for row in cursor.fetchall()]

# Obtener NoControl_Alumno existentes
cursor.execute("SELECT NoControl FROM ALUMNO")
nocontrol_alumnos = [row[0] for row in cursor.fetchall()]

# Generar datos falsos y agregarlos a la tabla DOCUMENTO_ALUMNO
for _ in range(50):  # Cambia 10 por el número de registros que desees crear
    id_documento = random.choice(documento_ids)
    nocontrol_alumno = random.choice(nocontrol_alumnos)

    #Se crea un ejemplo de dato BLOB
    archivo_texto = fake.text()
    archivo_bytes = archivo_texto.encode('utf-8')
    archivo_blob = base64.b64encode(archivo_bytes)

    fecha_presentacion = fake.date_between(start_date='-3y', end_date='today')
    fecha_vencimiento = fake.date_between(start_date=fecha_presentacion, end_date='+1y') if random.random() > 0.5 else None
    observaciones = fake.text() if random.random() > 0.5 else None
    estado = random.choice(['Pendiente', 'Aprobado', 'Rechazado'])

    # Insertar datos en la tabla DOCUMENTO_ALUMNO
    cursor.execute("INSERT INTO DOCUMENTO_ALUMNO (ID_Documento, NoControl_Alumno, Archivo, FechaPresentacion, FechaVencimiento, Observaciones, Estado) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (id_documento, nocontrol_alumno, archivo_blob, fecha_presentacion, fecha_vencimiento, observaciones, estado))

# Confirmar cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()
